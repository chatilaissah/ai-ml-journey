# ===== 3. Name formatter =====
first = input("First name: ")
last = input("Last name: ")

first = first.strip().title()     # "  iSSaH " → "Issah"
last = last.strip().title()       # " chatILA" → "Chatila"

full_name = first + " " + last    # join with a space
initials = first[0] + "." + last[0] + "."   # [0] = first letter

print(f"Full name: {full_name}")
print(f"Initials: {initials}")
print()