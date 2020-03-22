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

The program should present you an interactive matplotlib window, in which you can draw in points by hand (left mouse click creates a point). Draw the behavior you want to have by adding a sufficiently large number of points (minimum 10 points, unless you decrease the polynomial degree n = 10 currently hardcoded in the source). Then close the window (e.g. press "q"). A second window should open, showing the resulting polynomial fit:

![Example](http://sebastian.stapelberg.de/documents/polyfit.jpg "Example")
