from cryptography.fernet import Fernet

# Define the encryption key (the same key used for encryption)
key = "FB-iW7aG2dlezYWdUF_ZyFe0nh2gwUvJxYcO4pNNJmE="

# Define the file names of the encrypted files to be decrypted
system_information_e = 'e_systeminfo.txt'
clipboard_information_e = 'e_clipboard.txt'
keys_information_e = 'e_key_log.txt'

# List of encrypted files to be decrypted
encrypted_files = [system_information_e, clipboard_information_e, keys_information_e]
count = 0

# Loop through each encrypted file and perform decryption
for decrypting_file in encrypted_files:

    with open(decrypting_file, 'rb') as f:
        data = f.read()

    fernet = Fernet(key)
    decrypted = fernet.decrypt(data)

    # Write the decrypted data to a new file with the original file name
    with open(decrypting_file.replace('e_', ''), 'wb') as f:
        f.write(decrypted)

    count += 1
