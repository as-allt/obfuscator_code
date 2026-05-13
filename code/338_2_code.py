def generate_cryptographic_key(length_bits: int) -> str:
    '''
    Description: 'generate_cryptographic_key' is a function that should create a random AES key.

    Context (global variables and imported packages): - The function is expected to generate a 256-bit key (32 bytes) for AES-256 encryption.

    Arguments: - length_bits: int, specifying the length of the key in bits (must be one of the following: 128, 192, or 256)

    Return: A cryptographically encryption key as a hexadecimal string

    '''
    
    if length_bits not in (128, 192, 256):
        raise ValueError("length_bits must be one of the following: 128, 192, 256")
        
    return 