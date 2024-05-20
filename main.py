#!/usr/bin/env python3
import argparse

from utils import (
    decrypt,
    encrypt,
    generate,
    push
)



def main():
    parser = argparse.ArgumentParser(description="Encrypt and decrypt .env files")
    parser.add_argument("action", choices=["encrypt", "decrypt", "generate-keys"], help="Action to perform")
    parser.add_argument("file", help="Path to the file", nargs='?', default=None)
    parser.add_argument("--key", help="Path to the key file", required=False)
    parser.add_argument("--repo", help="Path to the repo", required=False)
    parser.add_argument("--save-location", choices=["project_folder", "ssh_folder"], default="ssh_folder", help="Specify where to save the RSA key pair (only applicable for generate-keys)")

    args = parser.parse_args()

    if args.action == "generate-keys":
        generate.generate_keys(args.save_location)
    elif args.action == "encrypt":
        if args.file and args.key:
            encrypt.encrypt_file(args.file, args.key)
            if args.repo:
                push.push_to_github(args.repo, args.file + ".enc")
        else:
            print("Please provide the file and key paths.")
    elif args.action == "decrypt":
        if args.file and args.key:
            decrypt.decrypt_file(args.file, args.key)
        else:
            print("Please provide the file and key paths.")

if __name__ == "__main__":
    main()