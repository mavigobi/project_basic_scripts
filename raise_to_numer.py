# autora: mavigobi

from cmath import sqrt
import math
x = 4
n = 3

# Method 1
y = x ** n #típico
print("%d to the power %d is %d" % (x,n,y))

# Method 2
y = pow(x,n) #función potencia importada de math
print("%d to the power %d is %d" % (x,n,y))

# Method 3
y = math.pow(x,n) #libreria.funcion
print("%d to the power %d is %5.2f" % (x,n,y))