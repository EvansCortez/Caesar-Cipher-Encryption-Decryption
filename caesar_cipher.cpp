#include <iostream>
#include <string>
using namespace std;

// Encrypts text using a shift value
string encrypt(string text, int shift) {
    string encryptedText = "";
    for (char character : text) {
        if (isalpha(character)) {
            char base = islower(character) ? 'a' : 'A';
            encryptedText += (character - base + shift) % 26 + base;
        } else {
            encryptedText += character; // Non-alphabet characters remain unchanged
        }
    }
    return encryptedText;
}

// Decrypts text using a shift value
string decrypt(string text, int shift) {
    return encrypt(text, 26 - shift); // Decryption is just encryption with the inverse shift
}

int main() {
    cout << "Caesar Cipher Tool" << endl;

    while (true) {
        cout << "\n1. Encrypt\n2. Decrypt\n3. Exit" << endl;
        cout << "Choose an option (1/2/3): ";
        int choice;
        cin >> choice;
        cin.ignore(); // Consume the newline character

        if (choice == 1) {
            string plaintext;
            int shift;
            cout << "Enter the plaintext: ";
            getline(cin, plaintext);
            cout << "Enter the shift value: ";
            cin >> shift;
            string encryptedText = encrypt(plaintext, shift);
            cout << "Encrypted Text: " << encryptedText << endl;
        } else if (choice == 2) {
            string ciphertext;
            int shift;
            cout << "Enter the ciphertext: ";
            getline(cin, ciphertext);
            cout << "Enter the shift value: ";
            cin >> shift;
            string decryptedText = decrypt(ciphertext, shift);
            cout << "Decrypted Text: " << decryptedText << endl;
        } else if (choice == 3) {
            cout << "Exiting the program. Goodbye!" << endl;
            break;
        } else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }
    return 0;
}