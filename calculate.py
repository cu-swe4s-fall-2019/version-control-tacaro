import sys
import math_lib

a = int(sys.argv[1])
b = int(sys.argv[2])

c = math_lib.add(a, b)
d = math_lib.div(a, b)

print("\n\n...running the calculation...\n")
print("The sum of your inputs is " + str(c))
print("The quotient of your inputs is " + str(d))
print("\n\n")
