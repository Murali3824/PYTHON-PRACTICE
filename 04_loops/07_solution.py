#  7. Validate Input
# Problem: Keep asking the user for input until
# they enter a number between 1 and 10. 

while True:
    n = int(input("enter value between 1 and 10 : "))
    if 1 <= n <=10:
        print("thanks")
        break
    else:
        print("invalid")