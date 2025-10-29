import matplotlib.pyplot as plt
eps = float(input("Enter tolerance parameter for the stopping rule: "))
alpha = float(input("Enter tolerance parameter for the stepsize selectionin the interval (0,1): "))
while not 0 < alpha < 1:
    alpha = float(input("Enter tolerance parameter for the stepsize selectionin the interval (0,1): "))
beta = float(input("Enter the constant in which the stepsize is multiplied at each backtracking step in the interval (0,1): "))
while not 0 < beta < 1:
    beta = float(input("Enter the constant in which the stepsize is multiplied at each backtracking step in the interval (0,1): "))
s = float(input("Enter initial choice of stepsize: "))
x = [0, 0]

for i in range(2):
    x[i] = float(input("Enter the element of x0: ")) #Setting x0

x0 = x
Params = [0.000009, 0.00037, 0.001, 0.002, 0.005, 0.01]

"""
ParaNumber = int(input("How many parameters do you want to check? "))
Params = [] * n
for i in range(n)
    Params[i] = float(input("Enter your desired parameter: "))
"""

itrs = []
for par in sorted(Params):
    f = x[0] ** 2 + par * x[1] ** 2
    grad = [2 * x[0], 2 * par * x[1]]
    itr = 0
    
    while grad[0] ** 2 + grad[1] ** 2 > eps ** 2:
        itr += 1
        t = s
        
        while (x[0] - t * grad[0]) ** 2 + par * (x[1] - t * grad[1]) ** 2 - x[0] ** 2 - par * x[1] ** 2 > -alpha * t * (grad[0] ** 2 + grad[1] ** 2):
            t *= beta
            
        for i in range(2):
            x[i] -= t * grad[i]
    
        f = x[0] ** 2 + par * x[1] ** 2 
        grad = [2*x[0], 2 * par * x[1]]
    
    itrs.append(itr)
    x = x0

plt.plot(Params, itrs)
plt.scatter(Params, itrs)
plt.show()

        
