# Import the required Fernet class from the cryptography.fernet module
from cryptography.fernet import Fernet

# Generate a new random Fernet key using the Fernet.generate_key() method
key = Fernet.generate_key()

# Open a file named "encryption_key.txt" in binary write mode ('wb') to write the key to the file
file = open("encryption_key.txt", 'wb')

# Write the generated key to the file
file.write(key)

# Close the file after writing the key
file.close()
