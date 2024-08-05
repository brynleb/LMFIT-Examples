import os
import matplotlib.pyplot as plt
import numpy as np
import lmfit as lm

def Gaussian(x, amp, cen, wid, off):
	"""Simple model of 1D Gaussian function."""
	return amp * np.exp(-0.5*((x-cen)/wid)**2) + off

## True parameter values
amp, cen, wid, off = (2.3, -0.8, 1.5, 0.5)
off_noise = 0.05

x = np.linspace(-10, 10, 101)
y = Gaussian(x, amp, cen, wid, off) + np.random.normal(0., off_noise, x.size)

LoadPreviousFit  = True
ShowInitialGuess = True
FitResultFile    = 'Gauss_FitResult.sav'

if LoadPreviousFit and os.path.exists(FitResultFile):
	result = lm.model.load_modelresult(FitResultFile, funcdefs={'Gaussian': Gaussian})
else:
	model  = lm.Model(Gaussian)
	# params = model.make_params()

	# Parameter definitions, initial guess
	amp = lm.Parameter(name='amp', value=1., vary=True, min=0., max=5.)
	cen = lm.Parameter(name='cen', value=0., vary=True, min=-np.inf, max=np.inf)
	off = lm.Parameter(name='off', value=0., vary=True, min=-np.inf, max=np.inf)
	wid = lm.Parameter(name='wid', value=1., vary=True, min=0., max=5.)

	params = lm.Parameters()
	params.add_many(amp, cen, wid, off)

	result = model.fit(y, params, x=x)

	## Alternate implementation
	# result = model.fit(y, x=x, amp=2., cen=0., wid=1., off=0.5)

	lm.model.save_modelresult(result, FitResultFile)

print('---------------- Fit Report ----------------')
print(result.fit_report())

print('--------------- Pretty Print ---------------')
print(result.params.pretty_print())

print('--------------- Custom Print ---------------')
for val in result.params.values():
	print('{:s}\t{:.3f}\t{:.3f}'.format(val.name, val.value, val.stderr))

# fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(7,5), constrained_layout=True)

fig = plt.figure(figsize=(7,5), constrained_layout=True)
wratios, hratios = ([1], [1, 3])
gs  = fig.add_gridspec(nrows=2, ncols=1, width_ratios=wratios, height_ratios=hratios)
ax1 = fig.add_subplot(gs[1,0])
ax0 = fig.add_subplot(gs[0,0], sharex=ax1)
axs = [ax0, ax1]
plt.setp(ax0.get_xticklabels(), visible=False)

axs[0].set_ylabel(r'$y - f(x)$')
axs[1].set_xlabel(r'$x$')
axs[1].set_ylabel(r'$y$')

axs[0].plot(x, y-result.best_fit, color='black', marker='.', linestyle='', label='Residuals')
axs[1].plot(x, y, color='black', marker='.', linestyle='', label='Data')
axs[1].plot(x, result.best_fit, color='crimson', marker='', linestyle='-', label='Best fit')

if ShowInitialGuess:
	axs[1].plot(x, result.init_fit, color='royalblue', marker='', linestyle='-', label='Initial guess')

for ax in axs:
	ax.legend(loc='best')
	ax.grid()

plt.show()