class SimpleCryptosystem: #defines the SimpleCryptosystem class
    def __init__(self, encryption_key, mac_key): #defines the initializer method.
        #store the encryption and MAC keys.
        self.encryption_key = encryption_key
        self.mac_key = mac_key

    def encrypt(self, plaintext): #defines the encrypt method.
        ciphertext = caesar_encrypt(plaintext, self.encryption_key) #encrypts the plaintext using the Caesar cipher.
        mac = generate_mac(ciphertext, self.mac_key) #generates a MAC for the ciphertext.
        return ciphertext, mac #returns the encrypted message and its MAC.

    def decrypt(self, ciphertext, mac): #defines the decrypt method.
        if not verify_mac(ciphertext, self.mac_key, mac): # verifies the MAC.
            raise ValueError("MAC verification failed") #raises an error if MAC verification fails.
        
        plaintext = caesar_decrypt(ciphertext, self.encryption_key) #decrypts the ciphertext.
        
        return plaintext #returns the decrypted message.

# Usage

#defining the encryption and MAC keys
encryption_key = 3
mac_key = "secret_key"

cryptosystem = SimpleCryptosystem(encryption_key, mac_key) #creates an instance of the cryptosystem

# Encrypt
plaintext = "Hello, World!"
ciphertext, mac = cryptosystem.encrypt(plaintext) #encrypts the plaintext and generates a MAC.
print(f"Ciphertext: {ciphertext}") #print the encrypted message and MAC.
print(f"MAC: {mac}")

# Decrypt
try:
    decrypted_text = cryptosystem.decrypt(ciphertext, mac) #attempts to decrypt the message and verify the MAC.
    print(f"Decrypted text: {decrypted_text}")
except ValueError as e: #catches and prints any errors if MAC verification fails.
    print(e)
