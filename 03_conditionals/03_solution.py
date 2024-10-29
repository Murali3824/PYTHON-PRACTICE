# 3. Grade Calculator
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

score = int(input("Enter your score :"))

if  90 <= score <= 100 :
    print("Grade A")
elif 80 <= score <= 89 :
    print("Grade B")
elif 70 <= score <= 79 :
    print("Grade C")
elif 60 <= score <= 69 :
    print("Grade D")
else:
    print("FAIL")

# if score >= 90 :
#     grade = "A"
# elif score >= 80 :
#     grade = "B"
# elif score >= 70 :
#     grade = "C"
# elif score >= 60 :
#     grade = "D"
# else :
#     grade = "F"
# print("your grade is :", grade)
