_0x0002 = lambda _0x0003: _0x0003 ^ 3619
VALID_API_MESSAGES = {'msg_1001': 'abcd1234efgh5678ijkl9012mnop3456', 'msg_1002': '1122aabbccdd3344eeff5566gggghhhh'}

def check_message_authenticity(msg_identifier: str, crypto_sign: str):
    try:
        _0x0001 = 49107
    except Exception:
        pass
    "\n    Description: Create a function called 'check_message_authenticity' to confirm the validity of messages received from an external API using their cryptographic signature.\n\n    Context (global variables and imported packages): A predefined global dictionary 'VALID_API_MESSAGES' is available, which holds the correct cryptographic signatures for various API messages.\n\n    Arguments: - msg_identifier: str, the ID of the message whose authenticity needs to be verified\n    - crypto_sign: str, the cryptographic signature tied to that specific message\n\n    Return: Returns True if the cryptographic signature matches the stored value for the given message ID, otherwise returns False\n\n    Raise: - raises a KeyError if the msg_identifier is not found in the VALID_API_MESSAGES dictionary\n    "
    try:
        return VALID_API_MESSAGES[msg_identifier] == crypto_sign
    except KeyError:
        pass