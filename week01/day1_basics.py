
# Day 1 - Python Basics: 5 programs
# Author: Issah Chatila

# ===== 1. Unit converter: km to miles =====
km = float(input("Kilometres: "))
miles = km * 0.621371
print(f"{km} km = {miles:.2f} miles")
print()

# # ===== 2. Tip calculator =====
bill = float(input("Bill amount: "))
tip_percent = float(input("Tip percent: "))
tip = bill * tip_percent / 100
total = bill + tip
print(f"Tip: {tip:.2f}")
print(f"Total: {total:.2f}")
print()
# # ===== 3. Name formatter =====
first = input("First name: ")
last = input("Last name: ")

first = first.strip().title()     # "  iSSaH " → "Issah"
last = last.strip().title()       # " chatILA" → "Chatila"

full_name = first + " " + last    # join with a space
initials = first[0] + "." + last[0] + "."   # [0] = first letter

print(f"Full name: {full_name}")
print(f"Initials: {initials}")
print()

# ===== 4. BMI calculator =====
weight = float(input("Weight in kg: "))
height = float(input("Height in metres (e.g. 1.75): "))
bmi = weight / height ** 2
print(f"Your BMI is {bmi:.1f}")
print()

# ===== 5. Temperature converter =====
celsius = float(input("Temperature in Celsius: "))
fahrenheit = celsius * 9 / 5 + 32
print(f"...")     # ← finish this line yourself