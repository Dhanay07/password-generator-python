import random
import string

print("=== ADVANCE PASSWORD GENERATOR ===")

length = int(input("Enter Password Length: "))

use_numbers = input("Include numbers? (y/n): ")
use_symbols = input("Include symbols? (y/n): ")

letters = string.ascii_letters

if use_numbers == "y":
	letters += string.digits

if use_symbols == "y":
	letters += string.punctuation

password = "".join(random.choice(letters) for i in range(length))

print("Generated Password: ",password)