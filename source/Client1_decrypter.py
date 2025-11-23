#!/usr/bin/env python3
"""
Decrypter template for BlazingBunny
The server will replace:
  DECRYPTION_KEY = "qZF2bKGMp_s2dso9mbeWulsJaEC9tJRT8KD6pUrw2mI="
  CLIENT_NAME = "Client1"
with the actual values before writing the generated script.
"""

from cryptography.fernet import Fernet
import os
import sys

DECRYPTION_KEY = "qZF2bKGMp_s2dso9mbeWulsJaEC9tJRT8KD6pUrw2mI="
CLIENT_NAME = "Client1"

def validate_key(key_str):
    try:
        Fernet(key_str.encode())
        return True
    except Exception:
        return False

def decrypt_file(filepath, fernet):
    with open(filepath, "rb") as f:
        encrypted_data = f.read()
    plaintext = fernet.decrypt(encrypted_data)
    outpath = filepath + ".decrypted"
    with open(outpath, "wb") as out:
        out.write(plaintext)
    return outpath

def main():
    print("=====================================")
    print(f"  BlazingBunny Decrypter - {CLIENT_NAME}")
    print("=====================================\n")

    if not validate_key(DECRYPTION_KEY):
        print("[ERROR] Embedded decryption key is invalid.")
        sys.exit(1)

    f = Fernet(DECRYPTION_KEY.encode())

    if len(sys.argv) < 2:
        print("Usage:")
        print(f"  python3 {os.path.basename(__file__)} <encrypted file>")
        sys.exit(0)

    input_file = sys.argv[1]
    if not os.path.exists(input_file):
        print(f"[ERROR] File not found: {input_file}")
        sys.exit(1)

    try:
        out = decrypt_file(input_file, f)
        print("[SUCCESS] Decrypted to:", out)
    except Exception as e:
        print("[ERROR] Decryption failed:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
