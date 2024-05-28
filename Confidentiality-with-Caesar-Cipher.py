
def caesar_encrypt(plaintext, key): #defining the caesar_encrypt function, which takes a plaintext string and an integer key.
    ciphertext = "" #initializes an empty string to store the ciphertext
    
    #Loop through Plaintext
    for char in plaintext: #repeats over each character in the plaintext
        if char.isalpha(): #checks if the character is a letter
            shift = key % 26 #computes the shift value, ensuring it wraps around after 26
            code = ord(char) + shift #gets the ASCII value of the character, adds the shift, and stores it in code.
            if char.islower(): #checks if the character is lowercase. If the new code exceeds 'z', it wraps around.
                if code > ord('z'): 
                    code -= 26
            elif char.isupper(): #checks if the character is uppercase. If the new code exceeds 'Z', it wraps around.
                if code > ord('Z'):
                    code -= 26
            ciphertext += chr(code) #converts the new code back to a character and appends it to the ciphertext.
        else: #non-alphabetic characters are appended to the ciphertext unchanged.
            ciphertext += char
    return ciphertext #returns the encrypted message

def caesar_decrypt(ciphertext, key): #defines the caesar_decrypt function.
    return caesar_encrypt(ciphertext, -key) #calls the caesar_encrypt function with the negative key to decrypt.