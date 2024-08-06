import random

chars = "qwertyuioplkjhgfdsazzxcvbnm,./!@#$%^&*()_1234567890"

password = ""

for i in range(16):
    password += random.choice(chars)

print(f"Tu contraseña es {password} ")