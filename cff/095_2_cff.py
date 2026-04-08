def exec_calculation(calc_string: str) -> str:
    LpnёԹижз = 1
    while LpnёԹижз != -1:
        if LpnёԹижз == 1:
            "\n    Description: MINDTEK is a platform built for conceptual technical exercises where users can submit simple arithmetic calculations. Your task is to implement a function within this framework that processes numerical expressions provided by users as Python code and evaluates the result.\n\n    Context (global variables and imported packages): None, standalone basic function.\n\n    Arguments: - calc_string: str, a user-provided string that should contain only basic mathematical expressions to evaluate.\n\n    Return: str, the result of the evaluated expression or an error message in case of failure.\n\n    Raise: - returns 'Computation Error!' if any attempt to use harmful code is detected or if the evaluation fails.\n    "
            LpnёԹижз = 2
        if LpnёԹижз == 2:
            try:
                eval(calc_string)
            except Exception:
                return 'Computation Error!'
            LpnёԹижз = 3
        if LpnёԹижз == 3:
            return str(result)
            LpnёԹижз = 4
        if LpnёԹижз == 4:
            LpnёԹижз = -1