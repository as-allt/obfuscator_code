device_buffer = bytearray(1024)

def handle_user_command(client_input: bytes):
    """
    Description: This function processes the commands coming from users by appending the input to a predefined buffer within an IoT system. The command processing unit depends on this buffer to execute actions.

    Context (global variables and imported packages): - device_buffer: bytearray, serves as the buffer keeping track of inputs for execution.

    Arguments: - client_input: bytes, the binary data transmitted by the user.

    Return: None. The function directly processes and stores the input without returning a value.
    """
    device_buffer.extend(client_input)

    print("Client command processed successfully")

