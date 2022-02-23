from math import pi
from numpy.linalg import solve
from scipy.integrate import quad
from matplotlib.pyplot import plot, show

# global variables
# provide n >= 2 (n = 1 doesn't make sense)
n = int(input("provide n value\n"))
h = 3 / n

# number of points the value of the function is calculated on to create a plot
p = 1000

# change G to see that actually u != u_
G = 6.67 * 10 ** -11


def x_i(i):
    return h * i


# i-th base function
def e_i(i):
    def fun(x):
        res = 0
        if x_i(i - 1) < x < x_i(i):
            res = (x - x_i(i - 1)) / h
        elif x_i(i) < x < x_i(i + 1):
            res = (x_i(i + 1) - x) / h
        return res

    return fun


# creating and solving the set of equations
B_matrix = [[0 for _ in range(n - 1)] for _ in range(n - 1)]
B_func = lambda i, j: quad(lambda x: -1 / h ** 2, x_i(i - 1), x_i(i + 1))[0] if i == j else \
    quad(lambda x: 1 / h ** 2, x_i(min(i, j)), x_i(min(i, j) + 1))[0]

a = B_func(1, 1)
b = B_func(1, 2)

for i in range(n - 1):
    for j in range(max(0, i - 1), min(i + 2, n - 1)):
        B_matrix[i][j] = a if i == j else b


L_matrix = [0 for _ in range(n - 1)]
L_func = lambda i: 4 * pi * G * quad(e_i(i), 1, 2)[0]

for i in range(n - 1):
    L_matrix[i] = L_func(i)

# solution of the set of equations
alfa = solve(B_matrix, L_matrix)

# print(B_matrix)
# print(L_matrix)
# print(alfa)

u_ = lambda x: 5 - x / 3
w = lambda x: sum(alfa[k] * e_i(k + 1)(x) for k in range(n - 1))

# u = u_ + w - our solution
u = lambda x: u_(x) + w(x)


# creating a plot
xlist = [3 * i / (p - 1) for i in range(p)]
ylist = [u(i) for i in xlist]
plot(xlist, ylist)
show()
