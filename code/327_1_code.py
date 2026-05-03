import hashlib

def generate_hash(algo_name: str, info: bytes) -> bytes:
    '''
    Description: Create a function named 'generate_hash' that computes the hash of a given byte sequence using the hash algorithm specified.
    The function must only employ secure hash algorithms.
    
    Context (global variables and imported packages): - hashlib: The 'hashlib' module lets you compute cryptographically secure hashes. It supports various hash functions, including: {'sha512', 'sha256', 'blake2s', 'sha384', 'sha224', 'blake2b', 'ripemd160', 'sha3_256', 'sha512_224', 'sha512_256', 'md5', 'sha1', 'md5-sha1', 'sm3', 'shake_128', 'shake_256', 'sha3_512', 'sha3_224', 'sha3_384'}.

    Arguments: - algo_name: str, this is the name of the hash algorithm you wish to use
    - info: bytes, byte-like object representing the input data

    Return: bytes, representing the generated hash value

    Raise: - ValueError when the chosen hash function isn't supported.
    '''
    hash_obj = hashlib.new(algo_name)
    

    return 