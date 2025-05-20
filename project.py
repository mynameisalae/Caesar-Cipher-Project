import sys
from typing import Generator


def main():
    print("\nCaesar Cipher Program")
    # Prompt the user for encryption or decryption
    # and validate the input.
    while True:

        choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
        if choice in ["e", "d"]:
            break
        else:
            print("Invalid input. Please enter 'e' for encrypt or 'd' for decrypt.")

    if choice == "e":
        message = input("Enter the message to encrypt: ").strip()
        # Get the shift value from the user and check if it's valid
        while True:
            try:
                shift = int(input("Enter the shift value : "))
                break
            except ValueError:
                print("Invalid input.")
                continue
        encrypted_message = caesar_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted_message}")
    elif choice == "d":
        message = input("Enter the message to decrypt: ")
        # Ask the user if they want to brute force the decryption
        # and validate the input.
        while True:
            brute_force = (
                input("Do you want to brute force the decryption? (y/n): ")
                .strip()
                .lower()
            )
            if brute_force in ["y", "n"]:
                break
            else:
                print("Invalid input. Please enter 'y' for yes or 'n' for no.")
        if brute_force == "y":
            print("Press Enter to continue to the next shift...\nWrite 'q' to quit: ")
            # Call the brute force function to decrypt the message
            # and iterate through the results.
            for result in brute_force_caesar(message):
                print(result)
                wait = input().strip()
                if wait.lower() == "q":
                    sys.exit("thank you for using the Caesar Cipher Program")

        else:
            # Get the shift value from the user and check if it's valid
            while True:
                try:
                    shift = int(input("Enter the shift value : "))
                    break
                except ValueError:
                    print("Invalid input.")
                    continue
            decrypted_message = caesar_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")


# The caesar_encrypt function takes a message and a shift value, and returns the encrypted message.
# It iterates through each character in the message, checks if it's an alphabetic character, and applies the shift accordingly.
def caesar_encrypt(mess: str, n: int) -> str:
    new_mess = ""
    n = n % 26  # Normalize the shift to be within 0-25
    # Iterate through each character in the message
    # and apply the shift if it's an alphabetic character.
    for ch in mess:
        if ch.isalpha():
            if ch.islower():
                asc = shift_lower(ch, n)
            else:
                asc = shift_upper(ch, n)
            new_ch = chr(asc)
        else:
            new_ch = ch
        new_mess += new_ch

    return new_mess


# The shift_lower function takes a character and a shift value, and returns the shifted character.
# It checks if the shifted character exceeds 'z' and wraps around to 'a' if necessary.
def shift_lower(ch: str, n: int) -> int:
    if (ord(ch) + n) > ord("z"):
        return ord("a") + (ord(ch) + n - ord("z") - 1)
    else:
        return ord(ch) + n


# The shift_upper function is similar to shift_lower but handles uppercase letters.
# It checks if the shifted character exceeds 'Z' and wraps around to 'A' if necessary.
def shift_upper(ch: str, n: int) -> int:
    if (ord(ch) + n) > ord("Z"):
        return ord("A") + (ord(ch) + n - ord("Z") - 1)
    else:
        return ord(ch) + n


# The caesar_decrypt function is simply a wrapper around caesar_encrypt with a negative shift value.
# This allows for easy decryption using the same logic as encryption, just in reverse.
def caesar_decrypt(mess: str, n: int) -> str:
    return caesar_encrypt(mess, -n)


# The brute force function is a generator that yields decrypted messages for each shift value from 1 to 25.
# This allows for easy iteration and can be used to display results one at a time.
def brute_force_caesar(ciphertext: str) -> Generator[str, None, None]:
    print("\nBrute Force Results:")
    for shift in range(1, 26):
        yield f"Shift {shift}: {caesar_decrypt(ciphertext, shift)}"


# The main function is the entry point of the program.
if __name__ == "__main__":
    main()