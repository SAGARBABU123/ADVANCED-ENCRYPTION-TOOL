from encryptor import Encryptor
import os

def main():
    print("==== Advanced Encryption Tool ====")
    option = input("1. Encrypt a file\n2. Decrypt a file\n3. Generate a key\nEnter your choice: ")

    encryptor = None

    if option == '3':
        encryptor = Encryptor()
        key = encryptor.get_key()
        print(f"Generated Key: {key.decode()}")
        with open("encryption_key.key", "wb") as key_file:
            key_file.write(key)
        print("Key saved to encryption_key.key")

    elif option == '1':
        key_file = input("Enter the key file path: ")
        if os.path.exists(key_file):
            with open(key_file, 'rb') as file:
                key = file.read()
            encryptor = Encryptor(key)
            file_path = input("Enter the file path to encrypt: ")
            if os.path.exists(file_path):
                encryptor.encrypt_file(file_path)
            else:
                print("Invalid file path.")
        else:
            print("Invalid key file path.")

    elif option == '2':
        key_file = input("Enter the key file path: ")
        if os.path.exists(key_file):
            with open(key_file, 'rb') as file:
                key = file.read()
            encryptor = Encryptor(key)
            file_path = input("Enter the encrypted file path to decrypt: ")
            if os.path.exists(file_path):
                encryptor.decrypt_file(file_path)
            else:
                print("Invalid file path.")
        else:
            print("Invalid key file path.")
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
