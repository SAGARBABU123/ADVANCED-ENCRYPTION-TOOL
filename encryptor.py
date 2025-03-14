from cryptography.fernet import Fernet

class Encryptor:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key()
        self.cipher = Fernet(self.key)

    def encrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted_data = self.cipher.encrypt(data)
        with open(file_path + '.enc', 'wb') as file:
            file.write(encrypted_data)
        print(f"File encrypted: {file_path}.enc")

    def decrypt_file(self, file_path):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = self.cipher.decrypt(encrypted_data)
        original_file = file_path.replace('.enc', '')
        with open(original_file, 'wb') as file:
            file.write(decrypted_data)
        print(f"File decrypted: {original_file}")

    def get_key(self):
        return self.key
