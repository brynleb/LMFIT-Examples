import matplotlib.pyplot as plt
import numpy as np
import lmfit as lm

plt.rc('axes', labelsize=14)
plt.rc('xtick', labelsize=14)
plt.rc('ytick', labelsize=14)
plt.rc('legend', fontsize=12)

x  = np.array([5., 8., 10., 11., 13., 14., 16., 19.])
y  = np.array([25.0, 31.2, 18.7, 27.8, 15.8, 21.1, 11.2, 17.8])
dy = np.array([4.8, 1.3, 5.4, 1.0, 4.8, 1.5, 7.3, 1.8])
w  = 1./dy**2

model  = lm.models.LinearModel()
# print(model.independent_vars, model.param_names)

result = model.fit(data=y, x=x, weights=w, slope=-1., intercept=30.)
print(result.fit_report())

sigy = result.eval_uncertainty(sigma=3)

## Plotting
_, axs = plt.subplots(nrows=1, ncols=1, figsize=(8,6), constrained_layout=True)

axs.errorbar(x, y, dy, color='black', ecolor='black', marker='o', linestyle='', label='data')
axs.plot(x, result.init_fit, color='crimson', marker='', linestyle='--', label='initial fit')
axs.plot(x, result.best_fit, color='royalblue', marker='', linestyle='-', label='best fit')
axs.fill_between(x, result.best_fit-sigy, result.best_fit+sigy, color='royalblue', alpha=0.5, label=r'3-$\sigma$ uncert')

axs.set_xlabel('Time (days)')
axs.set_ylabel('Distance (km)')

axs.set_xbound(0, 20)
axs.set_ybound(0, 45)
axs.grid()
axs.legend()

plt.show()