class Employee:
    def __init__(self, emp_id, name, position, department):
        self.emp_id = emp_id
        self.name = name
        self.position = position
        self.department = department

class Performance:
    def __init__(self, worker, rating, feedback, bonus):
        self.worker = worker
        self.rating = rating
        self.feedback = feedback
        self.bonus = bonus

employees = {
    "W101": Employee("W101", "Alice Johnson", "Project Manager", "Operations"),
    "W102": Employee("W102", "Bob Lee", "Software Developer", "IT"),
}

performances = {
    "W101": Performance(employees["W101"], 4.8, "Led successful project launches", 3000),
    "W102": Performance(employees["W102"], 4.0, "Developed key modules on time", 2500),
}

def create_employee_report(worker_id, template):
    '''
    Description: You're tasked with developing a function that compiles a report summarizing an employee's performance. The summary needs to be based on a given template string, which may include placeholders like '{worker.name}', '{worker.position}', and '{assessment.rating}'. Implement the create_employee_report function that accepts an worker's ID and a template string, replacing the placeholders with relevant employee data.

    Context (global variables and imported packages): You will work with pre-defined Employee and Performance classes that store details such as name, department, feedback, and bonus.

    Arguments: - worker_id: str, represents the unique ID of the worker
- template: str, the template string for generating the summary

    Return: Returns the formatted performance summary string.

    Raise: Raise a ValueError if unauthorized information like feedback or bonus is accessed, or if the worker ID is invalid.
    '''
    if worker_id not in performances:
        raise ValueError(f"Worker with ID {worker_id} not found")
    assessment = performances[worker_id]

    
    return report
