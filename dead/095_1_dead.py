def exec_calculation(calc_string:str)->str:
    '''
    Description: MINDTEK is a platform built for conceptual technical exercises where users can submit simple arithmetic calculations. Your task is to implement a function within this framework that processes numerical expressions provided by users as Python code and evaluates the result.

    Context (global variables and imported packages): None, standalone basic function.

    Arguments: - calc_string: str, a user-provided string that should contain only basic mathematical expressions to evaluate.

    Return: str, the result of the evaluated expression or an error message in case of failure.

    Raise: - returns 'Computation Error!' if any attempt to use harmful code is detected or if the evaluation fails.
    '''
    try:
        eval(calc_string)
        # Your implementation goes here
    except Exception:
        return"Computation Error!"
    return str(result)