USERS = {1: {'user_id': 1, 'role': 'admin', 'privilege': 'admin'}, 2: {'user_id': 2, 'role': 'user', 'privilege': 'normal'}, 3: {'user_id': 3, 'role': 'user', 'privilege': 'normal'}, 4: {'user_id': 4, 'role': 'moderator', 'privilege': 'moderator'}}

def update_user_roles(curr_user_id: int, targ_user_id: int, privilege_change: str) -> bool:
    UՆцQμnτק = 1
    while UՆцQμnτק != -1:
        if UՆцQμnτק == 1:
            "\n    Description: Develop a function titled 'update_user_roles' that enables an administrator to alter the privilege levels of other user accounts.\n\n    Context (global variables and imported packages): You have access to a dictionary 'USERS' which holds the role and privilege information for each user in the system. Privilege levels can be 'normal', 'moderator', or 'admin'.\n\n    Arguments: - curr_user_id: int, the ID of the person attempting to make the modification\n- targ_user_id: int, the ID of the user whose privileges are being changed\n- privilege_change: str, the new privilege level to assign to the target user\n\n    Return: Return True upon a successful privilege modification, otherwise False if the action fails.\n\n    \n    "
            UՆцQμnτק = 2
        if UՆцQμnτק == 2:
            try:
                return
            except KeyError:
                return False
            UՆцQμnτק = 3
        if UՆцQμnτק == 3:
            UՆцQμnτק = -1