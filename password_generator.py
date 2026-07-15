# Password Generator

import random
import string

print("===== Password Generator =====")

# Get password length from the user
length = int(input("Enter the desired password length: "))

# Character set
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display the password
print("\nGenerated Password:")
print(password)
