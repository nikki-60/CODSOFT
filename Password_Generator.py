import random
import string

def generate_password(length, password_type):
    characters = ''
    if 'lowercase' in password_type:
        characters += string.ascii_lowercase
    if 'uppercase' in password_type:
        characters += string.ascii_uppercase
    if 'digits' in password_type:
        characters += string.digits
    if 'special' in password_type:
        characters += string.punctuation

    if not characters:
        print("Please select at least one complexity option.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("!!!!Password Generator!!!!")
    try:
        length = int(input("Enter the desired length of the password: "))
        print("Enter password combinations or level of complexity like below.....")
        print("(lowercase/uppercase/digits/special)  if u want combination give combinations using commas like upperacse,digits and so on: ")
        password_type=input().split(",")
        password = generate_password(length, password_type)

        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter a valid length.")

if __name__ == "__main__":
    main()
