def generate_mac(message, key): #defines the generate_mac function.
    return simple_hash(message + key) #concatenates the message with the key and hashes the result using the simple_hash function.

def verify_mac(message, key, mac): #defines the verify_mac function.
    return generate_mac(message, key) == mac #generates a MAC for the message and key, and checks if it matches the provided MAC.