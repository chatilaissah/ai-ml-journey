# Day 2 - Conditionals
# Author: Issah Chatila

# ===== 1. Age eligibility checker =====
age = int(input("Enter your age: "))

if age < 18:
    print("You cannot vote or drive yet.")
elif age < 60:
    print("________________")      # ← ages 18 to 59
else:
    print("________________")      # ← ages 60 and above
print()