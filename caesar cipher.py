def caesar_cipher(text, shift, decrypt=False):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift
            if decrypt:
                shift_amount = -shift_amount
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

def main():
    while True:
        choice = input("Enter 'E' to encrypt or 'D' to decrypt: ").upper()
        if choice == 'E':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted_message)
        elif choice == 'D':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, shift, decrypt=True)
            print("Decrypted message:", decrypted_message)
        else:
            print("Invalid choice. Please enter 'E' or 'D'.")

        another = input("Do you want to perform another operation? (yes/no): ")
        if another.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
