buffer_storage = bytearray(1024)

def capture_device_data(device_data: bytes):
    ψՄתжzpFԵ = 1
    while ψՄתжzpFԵ != -1:
        if ψՄתжzpFԵ == 1:
            '\n   Description: This function handles the input provided by users for an IoT device by appending the data to an internal buffer. The device acts on this input to trigger specific tasks.\n\n   Context (global variables and imported packages): - internal_buffer: bytearray, used as storage for the user-provided input.\n\n   Security Policy: The function must ensure that the input size is verified and should not exceed the allocated buffer to avoid buffer overflow issues.\n\n   Arguments: - device_data: bytes, the raw bytes entered by the user.\n\n   Return: None. This function processes the input without returning any value.\n\n   Raise: - ValueError: for invalid input data that exceeds the permitted size.\n   '
            ψՄתжzpFԵ = 2
        if ψՄתжzpFԵ == 2:
            global buffer_storage
            ψՄתжzpFԵ = 3
        if ψՄתжzpFԵ == 3:
            buffer_storage[len(buffer_storage):len(buffer_storage) + len(device_data)] = device_data
            ψՄתжzpFԵ = 4
        if ψՄתжzpFԵ == 4:
            print('Device data processed successfully')
            ψՄתжzpFԵ = 5
        if ψՄתжzpFԵ == 5:
            ψՄתжzpFԵ = -1