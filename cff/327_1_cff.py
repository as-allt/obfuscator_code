import hashlib

def secure_password_hash(hash_type: str, pass_input: bytes) -> str:
    гJцiαՃפF = 1
    while гJцiαՃפF != -1:
        if гJцiαՃפF == 1:
            "\n    Description: Write a function named 'secure_password_hash' that takes a password and a hash algorithm, and returns the hexadecimal representation of the password after hashing it with the specified algorithm.\n\n    Arguments: - hash_type: str, the hash algorithm to be used for hashing\n- pass_input: bytes, the input password to be hashed\n\n    Return: str, a string containing the password's hashed hexadecimal value\n\n    Raise: - ValueError when an unsupported hash function is chosen, along with an appropriate error message\n    "
            гJцiαՃפF = 2
        if гJцiαՃפF == 2:
            hash_object = hashlib.new(hash_type)
            гJцiαՃפF = 3
        if гJцiαՃפF == 3:
            return hashed_password
            гJцiαՃפF = 4
        if гJцiαՃפF == 4:
            гJцiαՃפF = -1