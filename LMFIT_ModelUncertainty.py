import matplotlib.pyplot as plt
import numpy as np
import lmfit as lm

def Gaussian(x, amp, cen, wid):
	"""1-d Gaussian: gaussian(x, amp, cen, wid)"""
	return amp * np.exp(-0.5*((x-cen)/wid)**2)

x = np.linspace(-10, 10, 101)
y = Gaussian(x, 2.3, 0.2, 1.5) + np.random.normal(0, 0.1, x.size)

model  = lm.Model(Gaussian)
result = model.fit(y, x=x, amp=2., cen=0., wid=1.)

print(result.fit_report())

dy = result.eval_uncertainty(sigma=3)

plt.plot(x, y, 'bo')
plt.plot(x, result.init_fit, 'k--', label='initial fit')
plt.plot(x, result.best_fit, 'r-', label='best fit')
plt.fill_between(x, result.best_fit-dy, result.best_fit+dy,
                 color="#ABABAB", label=r'3-$\sigma$ uncertainty band')
plt.legend(loc='best')
plt.show()