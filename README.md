# FEM Solver
Python solver of the equation presented below usining Finite Element Method.
User should pass number of subdomains as input during operation of the program.

![equation](equation.jpg)

## Calculations

Mathematical paper with calculations used to obtain matrix form of the problem can be found [there](calculations_paper.pdf).

## Solution
Plot of the solution calculated using this [script](solver.py) where input value was 200.

<img src="plot.png" alt="plot" width="500"/>

## About G value
As G = 6.67 * 10<sup>-11</sup> which is approximately 0, the plot of the solution has to be a line segment.
Try changing [G value](solver.py#L15) to see that the script actually calculates the solution correctly.
Below plot of the solution where G=2 and input value was 200.

<img src="plot_G2.png" alt="plot" width="500"/>
