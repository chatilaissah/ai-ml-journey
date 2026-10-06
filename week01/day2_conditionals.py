# ===== 2. Grade calculator =====
score = float(input("Enter your score (0-100): "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 80:
    print("Grade: A")
elif score >= 70:
    print("Grade: B")
# ← add the C grade here (60 and above)
# ← add the D grade here (50 and above)
else:
    print("Grade: F")
print()