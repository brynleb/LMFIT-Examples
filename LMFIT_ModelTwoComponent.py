import matplotlib.pyplot as plt
import numpy as np
import lmfit as lm

def Line(x, slope, offset):
    """a line"""
    return slope*x + offset

def Gaussian(x, amp, cen, wid):
	"""1-d Gaussian: Gaussian(x, amp, cen, wid)"""
	return amp * np.exp(-0.5*((x-cen)/wid)**2)

pInit = lm.Parameters()
pInit.add_many(
	lm.Parameter('amp', value=2., min=0.),
	lm.Parameter('cen', value=0.),
	lm.Parameter('wid', value=1., min=0.),
	lm.Parameter('slope', value=0.),
	lm.Parameter('offset', value=1.)
)

model = lm.Model(Gaussian) + lm.Model(Line)
# pars  = model.make_params(amp=2, cen=0, wid=1, slope=0, offset=1)

model.set_param_hint('amp', value=pInit['amp'].value)
model.set_param_hint('cen', value=pInit['cen'].value)
model.set_param_hint('wid', value=pInit['wid'].value)
model.set_param_hint('slope', value=pInit['slope'].value)
model.set_param_hint('offset', value=pInit['offset'].value)
pars = model.make_params()

x = np.linspace(-10, 10, 101)
y = Gaussian(x, 2.3, 0.2, 1.5) + Line(x, 0.25, 1.) + np.random.normal(0, 0.1, x.size)

result = model.fit(y, pars, x=x)

print(result.fit_report())

plt.plot(x, y, 'bo')
plt.plot(x, result.init_fit, 'k--', label='initial fit')
plt.plot(x, result.best_fit, 'r-', label='best fit')
plt.legend(loc='best')
plt.show()