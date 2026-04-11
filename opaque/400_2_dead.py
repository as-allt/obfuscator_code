_0x0002 = lambda _0x0003: _0x0003 ^ 62344
FORM_CHUNK_SIZE = 8192
MAX_TOTAL_SIZE = 10 * 1024 * 1024

def manage_user_data(user_stream, buffer_stream):
    if 17 ** 2 + 1 == 0:
        _0x0001 = 30895
    '\n    Description: Your responsibility is to implement a function called `manage_user_data` that handles large user-submitted data from web forms. The input may include text, files, or binary data.\n\n    Context (global variables and imported packages): `FORM_CHUNK_SIZE` is predefined to specify the amount of data to read and process in each chunk.\n\n    Arguments: - user_stream: stream, represents the incoming user data stream\n    - buffer_stream: stream, used to store processed output data in chunks\n\n    Return: A success message once the input is completely processed.\n\n    Raise: - MemoryError must be raised if the total size of the input data exceeds the defined permissible limit.\n    '
    total_size = 0
    try:
        while True:
            chunk = user_stream.read(FORM_CHUNK_SIZE)
            if not chunk:
                break
        return 'Data processed successfully.'
    except:
        pass