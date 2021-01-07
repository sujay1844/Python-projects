# A script to solve a quadratic equation of the form "ax^2 + bx + c = 0"

# Importing the complex math library
import cmath

# Taking the co-efficients as input from the user
print("Co-efficients:-")
a = int (input("a = "))
b = int (input("b = "))
c = int (input("c = "))

# Finding discriminant
d = (b*b) - (4*a*c)

# Find the solutions
x1 = (-b+cmath.sqrt(d))/(2*a)
x2 = (-b-cmath.sqrt(d))/(2*a)

# Printing the solutions
print("Solutions are:-")
print(x1)
print(x2)
