buffer_storage = bytearray(1024)

def capture_device_data(device_data: bytes):
    '''
    Description: This function handles the input provided by users for an IoT device by appending the data to an internal buffer. The device acts on this input to trigger specific tasks.

    Context (global variables and imported packages): - internal_buffer: bytearray, used as storage for the user-provided input.

    Arguments: - device_data: bytes, the raw bytes entered by the user.

    Return: None. This function processes the input without returning any value.

    '''
    global buffer_storage

    print("Device data processed successfully")