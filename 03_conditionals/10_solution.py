# 10. Pet Food Recommendation
# Problem: Recommend a type of pet food based on the pet's species and age.
# (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet = input("enter type of pet : ")
age = int(input("enter age of pet : "))

if pet == "dog" :
    if age < 2 :
        food = "puppy food"
if pet == "cat" :
    if age > 5 :
        food = "senior cat food"
print("your pet food is : ", food)