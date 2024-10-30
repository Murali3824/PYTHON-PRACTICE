#  5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character. 

str = "madams"

for i in str:
    if str.count(i) == 1:
        print("first non repeated character : ",i)
        break