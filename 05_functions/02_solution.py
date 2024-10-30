#  2. Function with Multiple Parameters
# Problem: Create a function that takes two numbers as parameters and returns their sum. 

a = int(input("enter value of a : "))
b = int(input("enter value of b : "))

def sum(a, b):
    return a+b

print("sum of a and b is : ",sum(a, b))