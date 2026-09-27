import random
import string

# Get user input
length = int(input("Enter password length: "))
num_symbols = int(input("Enter number of symbols: "))
num_numbers = int(input("Enter number of numbers: "))

# Validate input
num_letters = length - num_symbols - num_numbers

if num_letters < 0:
    print("Error: Symbols + numbers cannot exceed the password length.")
else:
    # Character sets
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    # Generate the required characters
    password_chars = (
        random.choices(letters, k=num_letters)
        + random.choices(numbers, k=num_numbers)
        + random.choices(symbols, k=num_symbols)
    )

    # Shuffle them so the character types aren't grouped together
    random.shuffle(password_chars)

    password = ''.join(password_chars)

    print("Generated password:", password)
