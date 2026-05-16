# Password Generator 

import random
import string

print("🔐 Password Generator\n")

# Step 1: User input
length = int(input("Enter the desired password length: "))

# Step 2: Character set
characters = string.ascii_letters + string.digits + string.punctuation

# Step 3: Generate password
password = ""
for i in range(length):
    password += random.choice(characters)

# Step 4: Display result
print("\n✅ Generated Password:", password)
