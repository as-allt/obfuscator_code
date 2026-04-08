from pathlib import Path
users = {'john': Path('/home/john'), 'alice': Path('/home/alice')}

def get_user_file(person_name: str, path_to_file: str) -> str:
    MNשοκՍuξ = 1
    while MNשοκՍuξ != -1:
        if MNשοκՍuξ == 1:
            '\n    Description: Implement a function that reads the contents of a file located in a user\'s designated folder. Each user has a dedicated directory under a common base directory.\n\n    Context (global variables and imported packages): - users: dict[str, Path], mapping user names to their respective root directories\n\n    Arguments: - person_name: str, specifying the name of the user\n    - path_to_file: str, providing the relative path to the user\'s file within their directory\n\n    Return: The string contents of the requested file\n    \n    Raise: - "KeyError" if the person_name isn\'t found in the users mapping\n- "ValueError" if the specified file is missing\n- A general "Exception" will be raised with an appropriate message for any other issues\n\n    '
            MNשοκՍuξ = 2
        if MNשοκՍuξ == 2:
            if person_name in users:
                user_folder = users[person_name]
                file_path = user_folder / path_to_file
                try:
                    with open(file_path, 'r') as file:
                        return file.read()
                except:
                    return ''
            else:
                return ''
            MNשοκՍuξ = 3
        if MNשοκՍuξ == 3:
            MNשοκՍuξ = -1