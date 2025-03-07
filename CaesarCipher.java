import java.util.Scanner;

public class CaesarCipher {

    // Encrypts text using a shift value
    public static String encrypt(String text, int shift) {
        StringBuilder encryptedText = new StringBuilder();
        for (char character : text.toCharArray()) {
            if (Character.isLetter(character)) {
                char base = Character.isLowerCase(character) ? 'a' : 'A';
                encryptedText.append((char) ((character - base + shift) % 26 + base));
            } else {
                encryptedText.append(character); // Non-alphabet characters remain unchanged
            }
        }
        return encryptedText.toString();
    }

    // Decrypts text using a shift value
    public static String decrypt(String text, int shift) {
        return encrypt(text, 26 - shift); // Decryption is just encryption with the inverse shift
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Caesar Cipher Tool");

        while (true) {
            System.out.println("\n1. Encrypt\n2. Decrypt\n3. Exit");
            System.out.print("Choose an option (1/2/3): ");
            int choice = scanner.nextInt();
            scanner.nextLine(); // Consume the newline character

            if (choice == 1) {
                System.out.print("Enter the plaintext: ");
                String plaintext = scanner.nextLine();
                System.out.print("Enter the shift value: ");
                int shift = scanner.nextInt();
                String encryptedText = encrypt(plaintext, shift);
                System.out.println("Encrypted Text: " + encryptedText);
            } else if (choice == 2) {
                System.out.print("Enter the ciphertext: ");
                String ciphertext = scanner.nextLine();
                System.out.print("Enter the shift value: ");
                int shift = scanner.nextInt();
                String decryptedText = decrypt(ciphertext, shift);
                System.out.println("Decrypted Text: " + decryptedText);
            } else if (choice == 3) {
                System.out.println("Exiting the program. Goodbye!");
                break;
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        }
        scanner.close();
    }
}