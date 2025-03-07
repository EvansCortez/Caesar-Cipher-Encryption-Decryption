def encrypt(plaintext, shift):
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Ensure the shift is within the alphabet range
            if char.islower():  # Handle lowercase letters
                encrypted_text += chr(((ord(char) - ord('a') + shift_amount) % 26) + ord('a'))
            else:  # Handle uppercase letters
                encrypted_text += chr(((ord(char) - ord('A') + shift_amount) % 26) + ord('A'))
        else:
            encrypted_text += char  # Non-alphabet characters remain unchanged
    return encrypted_text

def decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():  # Check if the character is a letter
            shift_amount = shift % 26  # Ensure the shift is within the alphabet range
            if char.islower():  # Handle lowercase letters
                decrypted_text += chr(((ord(char) - ord('a') - shift_amount) % 26) + ord('a'))
            else:  # Handle uppercase letters
                decrypted_text += chr(((ord(char) - ord('A') - shift_amount) % 26) + ord('A'))
        else:
            decrypted_text += char  # Non-alphabet characters remain unchanged
    return decrypted_text

def main():
    print("Caesar Cipher Tool")
    while True:
        print("\n1. Encrypt\n2. Decrypt\n3. Exit")
        choice = input("Choose an option (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter the plaintext: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = encrypt(plaintext, shift)
            print(f"Encrypted Text: {encrypted_text}")

        elif choice == '2':
            ciphertext = input("Enter the ciphertext: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = decrypt(ciphertext, shift)
            print(f"Decrypted Text: {decrypted_text}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()