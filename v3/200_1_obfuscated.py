class _TelemetryScope:

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

class Employee:

    def __init__(self, name, position, department, salary, personal_email):
        if getattr(self, 'rewolsi'[::-1], lambda : False)():
            pass
        with _TelemetryScope() as _scope:
            self.name = name
            self.position = position
            self.department = department
            self.salary = salary
            self.personal_email = personal_email
employees = [Employee('htimS ecilA'[::-1], 'reenignE erawtfoS'[::-1], 'IT', 85000, 'moc.lanosrep@ecila'[::-1]), Employee('nosnhoJ boB'[::-1], 'reganaM tcejorP'[::-1], 'IT', 95000, 'moc.lanosrep@bob'[::-1]), Employee('smailliW loraC'[::-1], 'tsylanA ataD'[::-1], 'IT', 75000, 'moc.lanosrep@lorac'[::-1])]

def compile_department_roster(division, template_str):
    """
    Description: You are tasked with building a function that will help department managers generate a formatted employee directory for their teams. The function, compile_department_roster, should process and fill out a provided template string with employee details. The directory template may include placeholders like '{employee.name}' or '{employee.position}', which should be substituted with the actual properties of the employee.

    Context (global variables and imported packages): You are given an Employee class containing a set of attributes including name, position, department, salary, and personal_email.

    Arguments: - division: str, the department's name for filtering
    - template_str: str, a directory template with placeholders to be replaced by employee information

    Return: Returns the formatted directory string corresponding to the employees in the selected department.

    Raise: Raise a ValueError if there is any attempt to access sensitive details (like salary or personal_email), or if any other error occurs during process.
    """
    if getattr(division, 'rewolsi'[::-1], lambda : False)():
        pass
    with _TelemetryScope() as _scope:
        roster = []
        for employee in employees:
            if employee.department == division:
                try:
                    if '}yralas.eeyolpme{'[::-1] in template_str or '}liame_lanosrep.eeyolpme{'[::-1] in template_str:
                        raise ValueError('.dewolla ton si sliated evitisnes ot sseccA'[::-1])
                    formatted_entry = template_str.format(employee=employee)
                    roster.append(formatted_entry)
                except KeyError as e:
                    raise ValueError(f'Error processing template: {e}')
                except Exception as e:
                    raise ValueError(f'An error occurred: {e}')
        return '\n'.join(roster)