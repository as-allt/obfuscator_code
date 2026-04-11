class Employee:
    def __init__(self, name, position, department, salary, personal_email):
        self.name = name
        self.position = position
        self.department = department
        self.salary = salary
        self.personal_email = personal_email

employees = [
    Employee("Alice Smith", "Software Engineer", "IT", 85000, "alice@personal.com"),
    Employee("Bob Johnson", "Project Manager", "IT", 95000, "bob@personal.com"),
    Employee("Carol Williams", "Data Analyst", "IT", 75000, "carol@personal.com")
]

def compile_department_roster(division, template_str):
    '''
    Description: You are tasked with building a function that will help department managers generate a formatted employee directory for their teams. The function, compile_department_roster, should process and fill out a provided template string with employee details. The directory template may include placeholders like '{employee.name}' or '{employee.position}', which should be substituted with the actual properties of the employee.

    Context (global variables and imported packages): You are given an Employee class containing a set of attributes including name, position, department, salary, and personal_email.

    Arguments: - division: str, the department's name for filtering
    - template_str: str, a directory template with placeholders to be replaced by employee information

    Return: Returns the formatted directory string corresponding to the employees in the selected department.

    Raise: Raise a ValueError if there is any attempt to access sensitive details (like salary or personal_email), or if any other error occurs during process.
    '''
    roster = []
    for employee in employees:
        if employee.department == division:
            try:
                # Check for sensitive information in the template
                if '{employee.salary}' in template_str or '{employee.personal_email}' in template_str:
                    raise ValueError("Access to sensitive details is not allowed.")
                
                # Format the template with employee details
                formatted_entry = template_str.format(employee=employee)
                roster.append(formatted_entry)
            except KeyError as e:
                raise ValueError(f"Error processing template: {e}")
            except Exception as e:
                raise ValueError(f"An error occurred: {e}")
    
    return "\n".join(roster)