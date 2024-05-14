# EnvManager

EnvManager is a CLI tool written in Python that helps developers securely push their `.env` files to production or GitHub. The tool encrypts the `.env` files using a hybrid encryption method, ensuring sensitive information is not exposed accidentally. A better way to push your .env files to production without leaking your secret keys.

## Features

- Generate RSA key pairs for encryption and decryption.
- Encrypt `.env` files using AES encryption with an RSA-encrypted AES key.
- Decrypt `.env` files.
- Optionally push encrypted `.env` files to a GitHub repository.
- [Installation](#installation)
- [Usage](#usage)

  - [Generate RSA Key Pair](#generate-rsa-key-pair)
  - [Encrypt a `.env` File](#encrypt-a-env-file)
  - [Decrypt a `.env` File](#decrypt-a-env-file)
  - [Encrypt and Push to GitHub](#encrypt-and-push-to-github)
- [Directory Structure](#directory-structure)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Installation

1. Clone the repository:
    ```
        git clone https://github.com/yourusername/EnvManager.git
        cd EnvManager
    ```

2. Setup the package:
    ```
        bash setup.sh
    ```

## Usage

### Generate RSA Key Pair

    Generate a new RSA key pair for encryption and decryption:
        ```
            envmanager generate-keys
        ```

    This command will create `private.pem` and `public.pem` files in the current directory.

### Encrypt a `.env` File

    Encrypt a `.env` file using the public key:
        ```
            envmanager encrypt .env --key public.pem
        ```

    This will create an encrypted file named `.env.enc`.

### Decrypt a `.env` File

    Decrypt a `.env.enc` file using the private key:
        ```
            envmanager decrypt .env.enc --key private.pem
        ```

    This will create a decrypted file named `.env`.

### Encrypt and Push to GitHub

Encrypt a `.env` file and push the encrypted file to a GitHub repository:


## Directory Structure

EnvManager/
├── main.py
├── requirements.txt
├── README.md
└── utils/
    └── encrypt.py
    └── decrypt.py
    └── generate.py
    └── push.py

## Requirements

* Python 3.6+
* [pycryptodome](https://pypi.org/project/pycryptodome/)
* [GitPython](https://pypi.org/project/GitPython/)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

### Contributing Guide

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

## Acknowledgments

* This project uses [pycryptodome](https://pypi.org/project/pycryptodome/) for cryptographic functions.
* This project uses [GitPython](https://pypi.org/project/GitPython/) for Git operations.
