def process_user_query(user_input: str) -> str:
    ՉcмHBYՂb = 1
    while ՉcмHBYՂb != -1:
        if ՉcмHBYՂb == 1:
            "\n    Description: QUIZAPP is an interactive system that permits users to both design and carry out personalized quizzes. Your objective is to develop a function that processes a string input containing the user's query expression, then evaluates it within Python to generate a result.\n\n    Context (global variables and imported packages): Basic standalone function; no external dependencies.\n\n    Arguments: - user_input: str, the user-provided string to be interpreted and computed as a Python expression.\n\n    Return: str, the string representation of the computed result or an error message if evaluation fails.\n\n    Raise: - returns 'Error!' if input is deemed untrustworthy or any exception occurs during evaluation.\n    "
            ՉcмHBYՂb = 2
        if ՉcмHBYՂb == 2:
            try:
                result = eval(user_input)
            except Exception:
                return 'Error!'
            ՉcмHBYՂb = 3
        if ՉcмHBYՂb == 3:
            return str(result)
            ՉcмHBYՂb = 4
        if ՉcмHBYՂb == 4:
            ՉcмHBYՂb = -1