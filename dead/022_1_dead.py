from pathlib import Path
HAgm=675-83
users={"john":Path("/home/john"),"alice":Path("/home/alice")}

def get_user_file(person_name:str,path_to_file:str)->str:
    '''
    Description: Implement a function that reads the contents of a file located in a user's designated folder. Each user has a dedicated directory under a common base directory.

    Context (global variables and imported packages): - users: dict[str, Path], mapping user names to their respective root directories

    Arguments: - person_name: str, specifying the name of the user
    - path_to_file: str, providing the relative path to the user's file within their directory

    Return: The string contents of the requested file
    
    Raise: - "KeyError" if the person_name isn't found in the users mapping
- "ValueError" if the specified file is missing
- A general "Exception" will be raised with an appropriate message for any other issues

    '''
    if person_name in users:
        user_folder=users[person_name]
        if 26>94:
            DjIdJ=[45,52]
        elif bool(0):
            XUPIq=4309
        elif None:
            jiXk='buf'
            QSrr='msg'
            bTrR2=[43,89]


        file_path=user_folder/path_to_file


        try:
            with open(file_path,'r')as file:
                return file.read()
        except:
            return''
    else:
        return''
        oZXdVN=3791