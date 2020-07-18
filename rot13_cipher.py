#!/usr/bin/env python3
"""This python script rotates the ASCII text in the submitted file
with ROT13 Algorithm, either to encrypt or to decrypt the text."""

import os
import sys
from rot13_dict import rot_dict

def rot_file(filename, encrypted_file):
    "Returns the decrypted/encrypted file using the dictionary for rotating the letters."
    with open(filename) as file:
        with open(encrypted_file, "w") as cipher_file:
            read = file.read()
            for line in read:
                for letter in line:
                    if letter.isalpha():
                        cipher_file.write(rot_dict[letter])
                    else:
                        cipher_file.write(letter)

source = sys.argv[1]
destination = sys.argv[2]

if os.path.isfile(source):

    if '~' in source:
        source = os.path.expanduser('~') + source[1:]
    elif '~' in destination:
        destination = os.path.expanduser('~') + destination[1:]
    else:
        pass

elif os.path.isdir(source):
    print(f"{source} is a directory.")
    print("Submit a file in ASCII text format for its encryption.")
    sys.exit(1)

else:
    print(f"{source} doesn't exist.")
    print("Please submit a file existing in your computer!")
    sys.exit(1)

#Encrypting the plaintext file with ROT13 Subtitution Cipher:
rot_file(source, destination)

#Result:
print(f"Ciphertext location: {destination}")
sys.exit(0)
