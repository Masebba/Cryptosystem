def simple_hash(message): #defines the simple_hash function.
    hash_value = 0  #initializes the hash value to 0.

    #Loop
    for char in message: #Repeats over each character in the message.
        hash_value = (hash_value + ord(char)) % 256 #adds the ASCII value of the character to the hash value and takes the result modulo 256.
    return hash_value #returns the final hash value.