from cryptography.fernet import Fernet

def encrypt(plain_text):
    key = Fernet.generate_key() #this is your "password"
    cipher_suite = Fernet(key)
    encrypted = cipher_suite.encrypt(str.encode(plain_text))
    return encrypted, key

def decrypt(encoded_text, key):
    cipher_suite = Fernet(key)
    decrypted = cipher_suite.decrypt(encoded_text)
    return decrypted