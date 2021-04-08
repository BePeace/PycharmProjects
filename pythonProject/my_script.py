
import math
#from math import exp
#from math import exp as exponential
#from math import factorial
#from math import sum


from my_module import compute


numbers = [5,7,11]
#result = sum([math.factorial(n) for n in numbers])

result = 0
for n in numbers:
    result += math.factorial(n)
print(result)

print(compute ([5,7,11]))

print(math.exp(2))