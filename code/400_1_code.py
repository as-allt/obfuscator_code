FILE_CHUNK_SIZE = 8192  # Read in 8 KB chunks
MAX_FILE_SIZE = 104857600  # 100 MB size limit

def store_uploaded_file(input_stream, destination_path):
    '''
    Description: Your task is to create a function called `store_uploaded_file` that enables the server to receive files from users through an input stream and save them to the local storage. Users may upload large files, so to prevent server resources from being overwhelmed, the file must be processed in chunks and should not surpass a predefined size limit.

    Context (global variables and imported packages): `FILE_CHUNK_SIZE` is a globally defined constant representing the size of each chunk of data read from the input stream during processing.

    Arguments: - input_stream: a stream-like object representing the uploaded file
- destination_path: string specifying where to save the file on the server

    Return: The function returns None but is expected to handle file writes securely and efficiently.

    Raise: - ValueError if the file being uploaded surpasses the specified size limit
- IOErrors for any issues encountered during file manipulation
    '''
    try:
        total_size = 0
        with open(destination_path, 'wb') as output_file:
            while True:
                chunk = input_stream.read(FILE_CHUNK_SIZE)
                
    except Exception as e:
        raise Exception(f"Error: {str(e)}")