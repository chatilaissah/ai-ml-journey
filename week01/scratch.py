# ---- 1. The 4 basic data types ----
name = "issah chatila"   # str   = text (always in quotes)
age = 23                 # int   = whole number
height = 1.78            # float = decimal number
is_student = True        # bool  = True or False
print(type(height), type(is_student))

# ---- 2. Maths with numbers ----
print(10 + 3, 10 - 3, 10 * 3)   # 13 7 30
print(10 / 3)    # 3.333... normal division always gives a float
print(10 // 3)   # 3  floor division (drops the decimal)
print(10 % 3)    # 1  remainder
print(2 ** 3)    # 8  power

# ---- 3. String methods ----
print(name.title())        # Issah Chatila
print(name.upper())        # ISSAH CHATILA
print(len(name))           # number of characters
print("   hi   ".strip())  # removes spaces at both ends
print(name[0])             # first character: i
print(name.split())        # ['issah', 'chatila']

# ---- 4. f-strings and number formatting ----
price = 1234.5678
print(f"Price: {price:.2f}")       # 2 decimal places
print(f"Price: {price:,.2f}")      # with comma separators
print(f"Next year I'll be {age + 1}")

# ---- 5. Type conversion ----
print(int("25") + 5)     # text -> int
print(float("2.5") * 2)  # text -> float
print(str(age) + " years")   # int -> text, so it can join with text

# ---- 6. input() ALWAYS returns text ----
num = input("Enter a number: ")
print(type(num))         # <class 'str'>, even if you typed 5
num = float(num)
print(num * 2)