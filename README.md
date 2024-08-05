# LMFIT-Examples

Some useful examples of the LMFIT package for non-linear least-squares minimization and curve fitting in Python.

Initially inspired by (and named for) the Levenberg-Marquardt method from scipy.optimize.leastsq, LMFIT provides a high-level interface for non-linear optimization and curve fitting problems in Python with a number of useful enhancements, including:

- Using Parameter objects instead of plain floats as variables. A Parameter is Python object that:
  - has a value that can be varied during the fit or kept at a fixed value;
  - can have upper and/or lower bounds;
  - can have a value that is constrained by an algebraic expression of other Parameter values;
  - can have attributes associated with a fit result, such as a standard error for estimating uncertainties.

- Ease of changing fitting algorithms.
  - Once a fitting model is set up, one can change the fitting algorithm used to find the optimal solution without changing the objective function.

- Improved estimation of confidence intervals.
  - While scipy.optimize.leastsq will automatically calculate uncertainties and correlations from the covariance matrix, the accuracy of these estimates is sometimes questionable.
  - LMFIT has functions to explicitly explore parameter space and determine confidence levels even for the most difficult cases.
  - LMFIT can also use the numdifftools package to estimate parameter uncertainties and correlations for algorithms that do not natively support this in SciPy.

- Improved curve-fitting with the Model class.
  - An extention of the capabilities of scipy.optimize.curve_fit, allowing users to turn a function that models their data into a Python class that helps parameterize and fit data with that model.

- Many built-in models for common lineshapes, including:
  - Peak-like models, step-like models, polynomial models, periodic models, exponential and power-law models, and user-defined models.
  - See [Build-in models](https://lmfit.github.io/lmfit-py/builtin_models.html) for a complete list.

## List of examples



## Additional resources

- [LMFIT documentation](https://lmfit.github.io/lmfit-py/index.html)
- [LMFIT GitHub](https://github.com/lmfit/lmfit-py/)
