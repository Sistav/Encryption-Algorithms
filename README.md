# Encryption Algorithms

This Python package provides a comprehensive suite of encryption and decryption algorithms, including:

- **Substitution Cipher**: A method of encryption by which units of plaintext are replaced with ciphertext according to a fixed system.
- **Playfair Cipher**: An encryption technique that encrypts pairs of letters (digraphs), making it harder to decrypt without knowledge of the key.
- **Caesar Cipher**: A type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet.
- **Transposition Cipher**: A method of encryption by which the positions held by units of plaintext are shifted according to a regular system, so that the ciphertext constitutes a permutation of the plaintext.

## Features

- **Customizable Encryption & Decryption**: Each class method allows for customizable keys or shifts, providing flexibility in encryption strength.
- **Text Processing**: Handles uppercase conversion and exclusion of non-alphabetic characters to ensure consistent encryption and decryption processes.
- **Modular Design**: The `Message` class acts as a base for `plaintextMsg` and `ciphertextMsg` classes.

## Usage
```python
# Example usage for encrypting and decrypting a message using Caesar Cipher
from encryption_algorithms import plaintextMsg, ciphertextMsg

# Encrypt a message
encrypted_message = plaintextMsg("Hello World").caesarCipher(shift=3)

# Decrypt the message
decrypted_message = encrypted_message.caesarCipher(shift=-3)

print(decrypted_message.getText())  # Output: HELLO WORLD
```