import random
import string

print("=== PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))

letter = string.ascii_letters
number = string.digits
symbol = string.punctuation

all_characters = letter + number + symbol
password = ""

for i in range(length):
	password += random.choice(all_characters)

print("GENERATED PASSWORD: ",password)