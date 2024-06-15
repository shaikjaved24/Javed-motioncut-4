import random
import string

def generate_password(length, num_passwords):
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+-=[]{}|;:,.<>?'
    
    combined_characters = (
        list(uppercase_letters) +
        list(lowercase_letters) +
        list(digits) +
        list(special_characters)
    )
    
    passwords = []
    for _ in range(num_passwords):
        password = ''.join(random.choices(combined_characters, k=length))
        passwords.append(password)
    
    return passwords

if __name__ == "__main__":
    print("Welcome to the Strong Password Generator!")
    print("---------------------------------------")
    
    while True:
        try:
            length = int(input("Enter the length of the password(s): "))
            num_passwords = int(input("Enter the number of passwords to generate: "))
            
            if length <= 0 or num_passwords <= 0:
                print("Length and number of passwords must be greater than zero. Please try again.")
                continue
            
            generated_passwords = generate_password(length, num_passwords)
            
            print("\nGenerated Password(s):")
            for password in generated_passwords:
                print(password)
            
            break
        
        except ValueError:
            print("Invalid input. Please enter valid integers for length and number of passwords.")
            continue
