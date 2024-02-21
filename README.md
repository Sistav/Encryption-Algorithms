# Encryption Algorithms

This Python package provides a suite of encryption and decryption algorithms, including:

- **Substitution Cipher**: A method of encryption by which units of plaintext are replaced with ciphertext according to a fixed system.
- **Playfair Cipher**: An encryption technique that encrypts pairs of letters (digraphs), making it harder to decrypt without knowing the key.
- **Caesar Cipher**: A type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet.
- **Transposition Cipher**: A method of encryption by which the positions held by units of plaintext are shifted according to a regular system so that the ciphertext constitutes a permutation of the plaintext.

## Features

- **Customizable Encryption & Decryption**: Each class method allows for customizable keys or shifts, providing flexibility in encryption strength.
- **Text Processing**: Handles uppercase conversion and exclusion of non-alphabetic characters to ensure consistent encryption and decryption processes.
- **Modular Design**: The `Message` class is a base for the `plaintextMsg` and `ciphertextMsg` classes.
