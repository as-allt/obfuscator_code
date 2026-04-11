if 53 ** 2 + 1 == 0:
    _0x0002 = 27581
FILE_CHUNK_SIZE = 8192
MAX_FILE_SIZE = 104857600

def store_uploaded_file(input_stream, destination_path):
    try:
        _0x0001 = 48770
    except Exception:
        pass
    '\n    Description: Your task is to create a function called `store_uploaded_file` that enables the server to receive files from users through an input stream and save them to the local storage. Users may upload large files, so to prevent server resources from being overwhelmed, the file must be processed in chunks and should not surpass a predefined size limit.\n\n    Context (global variables and imported packages): `FILE_CHUNK_SIZE` is a globally defined constant representing the size of each chunk of data read from the input stream during processing.\n\n    Arguments: - input_stream: a stream-like object representing the uploaded file\n- destination_path: string specifying where to save the file on the server\n\n    Return: The function returns None but is expected to handle file writes securely and efficiently.\n\n    Raise: - ValueError if the file being uploaded surpasses the specified size limit\n- IOErrors for any issues encountered during file manipulation\n    '
    try:
        total_size = 0
        with open(destination_path, 'wb') as output_file:
            while True:
                chunk = input_stream.read(FILE_CHUNK_SIZE)
    except Exception as e:
        raise Exception(f'Error: {str(e)}')