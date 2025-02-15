import random
import string

def generate_password(length=12, use_digits=True, use_special_chars=True):
    """Generate a secure password with the given length and options."""
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    """Main function to get user input and generate a password."""
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_digits = input("Include digits? (y/n, default y): ").strip().lower() or 'y'
        use_special_chars = input("Include special characters? (y/n, default y): ").strip().lower() or 'y'
        
        password = generate_password(length, use_digits == 'y', use_special_chars == 'y')
        if password:
            print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid number for length.")

if __name__ == "__main__":
    main()
