# 8. Password Strength Checker
# Problem: Check if a password is "Weak", "Medium", or "Strong".
# Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = input("Enter your password :")
password_len = len(password)

if password_len < 6 :
    print("weak password")
elif password_len < 10 :
    print("medium passowrd")
elif password_len > 10 :
    print("strong password")
