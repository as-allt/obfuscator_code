if (63 & 1) + (63 >> 1 & 1) > 3:
    _0x0005 = 62610

class Employee:

    def __init__(self, name, position, department, salary, personal_email):
        _0x0001 = lambda _0x0002: _0x0002 ^ 19741
        self.name = name
        self.position = position
        self.department = department
        self.salary = salary
        self.personal_email = personal_email
employees = [Employee('Alice Smith', 'Software Engineer', 'IT', 85000, 'alice@personal.com'), Employee('Bob Johnson', 'Project Manager', 'IT', 95000, 'bob@personal.com'), Employee('Carol Williams', 'Data Analyst', 'IT', 75000, 'carol@personal.com')]

def compile_department_roster(division, template_str):
    _0x0003 = lambda _0x0004: _0x0004 ^ 39244
    "\n    Description: You are tasked with building a function that will help department managers generate a formatted employee directory for their teams. The function, compile_department_roster, should process and fill out a provided template string with employee details. The directory template may include placeholders like '{employee.name}' or '{employee.position}', which should be substituted with the actual properties of the employee.\n\n    Context (global variables and imported packages): You are given an Employee class containing a set of attributes including name, position, department, salary, and personal_email.\n\n    Arguments: - division: str, the department's name for filtering\n    - template_str: str, a directory template with placeholders to be replaced by employee information\n\n    Return: Returns the formatted directory string corresponding to the employees in the selected department.\n\n    Raise: Raise a ValueError if there is any attempt to access sensitive details (like salary or personal_email), or if any other error occurs during process.\n    "
    roster = []
    for employee in employees:
        if employee.department == division:
            try:
                if '{employee.salary}' in template_str or '{employee.personal_email}' in template_str:
                    raise ValueError('Access to sensitive details is not allowed.')
                formatted_entry = template_str.format(employee=employee)
                roster.append(formatted_entry)
            except KeyError as e:
                raise ValueError(f'Error processing template: {e}')
            except Exception as e:
                raise ValueError(f'An error occurred: {e}')
    return '\n'.join(roster)