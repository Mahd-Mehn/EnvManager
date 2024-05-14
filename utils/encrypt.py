from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

def encrypt_file(file_path, public_key_path):
    with open(public_key_path, "rb") as pub_file:
        public_key = RSA.import_key(pub_file.read())
    
    cipher_rsa = PKCS1_OAEP.new(public_key)
    
    # Generate a random AES key
    aes_key = get_random_bytes(32)  # AES-256
    
    # Encrypt the AES key with RSA
    encrypted_aes_key = cipher_rsa.encrypt(aes_key)
    
    # Read the plaintext file data
    with open(file_path, "rb") as f:
        file_data = f.read()
    
    # Encrypt the file data with AES
    cipher_aes = AES.new(aes_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(file_data)
    
    # Write the encrypted AES key and the encrypted file data to an output file
    with open(file_path + ".enc", "wb") as enc_file:
        for x in (cipher_aes.nonce, tag, encrypted_aes_key, ciphertext):
            enc_file.write(x)