# LMFIT-Examples

Some useful examples of the LMFIT package for non-linear least-squares minimization and curve fitting in Python

LMFIT provides a high-level interface to non-linear optimization and curve fitting problems for Python. It builds on and extends many of the optimization methods of scipy.optimize. Initially inspired by (and named for) extending the Levenberg-Marquardt method from scipy.optimize.leastsq, LMFIT now provides a number of useful enhancements to optimization and data fitting problems, including:

- Using Parameter objects instead of plain floats as variables. A Parameter has a value that can be varied during the fit or kept at a fixed value. It can have upper and/or lower bounds. A Parameter can even have a value that is constrained by an algebraic expression of other Parameter values. As a Python object, a Parameter can also have attributes such as a standard error, after a fit that can estimate uncertainties.

- Ease of changing fitting algorithms. Once a fitting model is set up, one can change the fitting algorithm used to find the optimal solution without changing the objective function.

- Improved estimation of confidence intervals. While scipy.optimize.leastsq will automatically calculate uncertainties and correlations from the covariance matrix, the accuracy of these estimates is sometimes questionable. To help address this, lmfit has functions to explicitly explore parameter space and determine confidence levels even for the most difficult cases. Additionally, lmfit will use the numdifftools package (if installed) to estimate parameter uncertainties and correlations for algorithms that do not natively support this in SciPy.

- Improved curve-fitting with the Model class. This extends the capabilities of scipy.optimize.curve_fit, allowing you to turn a function that models your data into a Python class that helps you parametrize and fit data with that model.

- Many built-in models for common lineshapes are included and ready to use.
