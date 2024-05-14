from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes

def decrypt_file(file_path, private_key_path):
    with open(private_key_path, "rb") as prv_file:
        private_key = RSA.import_key(prv_file.read())
    
    cipher_rsa = PKCS1_OAEP.new(private_key)
    
    # Read the encrypted file data
    with open(file_path, "rb") as enc_file:
        nonce, tag, encrypted_aes_key = [enc_file.read(x) for x in (16, 16, private_key.size_in_bytes())]
        ciphertext = enc_file.read()
    
    # Decrypt the AES key with RSA
    aes_key = cipher_rsa.decrypt(encrypted_aes_key)
    
    # Decrypt the file data with AES
    cipher_aes = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    file_data = cipher_aes.decrypt_and_verify(ciphertext, tag)
    
    # Write the decrypted file data to an output file
    with open(file_path.replace(".enc", ""), "wb") as dec_file:
        dec_file.write(file_data)