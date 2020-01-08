# polyfit (beta)

Small python3 script to find the closest polynomials to hand-drawn datapoints, just for fun.
The current version of the code is in a highly pre-mature state yet, as it is the result of a first test only. Upcoming improvements include e.g. a proper exception handling and a better way to set the polynomial degree, which at the moment is hardcoded in the source code.

# Requirements

- numpy
- scipy
- matplotlib

# Usage

```shell
$ chmod +x polyift
$ ./polyfit
```

The program should open an interactive matplotlib window in which you can draw points by clicking at a certain position. Draw a curve of points (must be N > 10, or change the polynomial degree n = 10 that is currently hardcoded in the source code) and close the window (e.g. press "q"). A second window should open, showing you the resulting polynomial fit.
