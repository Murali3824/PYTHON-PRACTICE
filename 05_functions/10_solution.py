#  10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number. 

num = int(input("enter a number : "))

def fact(num):
    if num == 0:
        return 1
    else:
        return num * fact(num-1) 
    
print(fact(num))

