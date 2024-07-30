import string
import random

def generate_password(length):
    if length < 4:  # Ensure there's enough length to include all character types
        return "Password length should be at least 4 characters."

    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password includes at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length with random choices from all sets
    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length-4)

    # Shuffle to ensure the characters are in random order
    random.shuffle(password)

    return ''.join(password)

# Ask the user for the desired password length
length = int(input("Enter the desired length for the password: "))
print(f"Generated password was: {generate_password(length)}")
