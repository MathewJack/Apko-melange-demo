#!/usr/bin/env python3

import base64
import sys

def encode(text):
    """Encodes the input text using base64."""
    return base64.b64encode(text.encode())

def decode(text):
    """Decodes the input text using base64."""
    return base64.b64decode(text).decode()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py [-e|-d] <text>")
        sys.exit(1)

    operation = sys.argv[1]
    text = sys.argv[2]

    if operation == '-e':
        encoded_text = encode(text)
        print("Encoded text:", encoded_text.decode())
    elif operation == '-d':
        decoded_text = decode(text)
        print("Decoded text:", decoded_text)
    else:
        print("Invalid operation. Please use -e for encode or -d for decode.")
        sys.exit(1)
