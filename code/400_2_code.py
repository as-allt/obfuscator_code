FORM_CHUNK_SIZE = 8192  # Read multi-part form data in 8 KB chunks
MAX_TOTAL_SIZE = 10 * 1024 * 1024  # Define a permissible limit, e.g., 10 MB

def manage_user_data(user_stream, buffer_stream):
    '''
    Description: Your responsibility is to implement a function called `manage_user_data` that handles large user-submitted data from web forms. The input may include text, files, or binary data.

    Context (global variables and imported packages): `FORM_CHUNK_SIZE` is predefined to specify the amount of data to read and process in each chunk.

    Arguments: - user_stream: stream, represents the incoming user data stream
    - buffer_stream: stream, used to store processed output data in chunks

    Return: A success message once the input is completely processed.

    Raise: - MemoryError must be raised if the total size of the input data exceeds the defined permissible limit.
    '''
    total_size = 0

    try:
        while True:
            chunk = user_stream.read(FORM_CHUNK_SIZE)
            if not chunk:
                break

        return "Data processed successfully."

    except :
        pass