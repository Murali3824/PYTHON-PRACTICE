# 1. Age Group Categorization
# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

age = int(input("Enter your age : "))

if age < 13:
    print("you are a child")
elif age < 20 :
    print("you are a teenager")
elif age < 60 :
    print("you are an adult")
else :
    print("you are a senior")