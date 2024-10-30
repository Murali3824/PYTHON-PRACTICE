#  6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop. 

n = 4
fact = 1

while n > 0:
    fact = fact * n
    n = n - 1
print('factorial is : ', fact)