import xml.etree.ElementTree as ET

def parse_staff_data(staff_xml: str):
    '''
    Description: Develop a function named 'parse_staff_data' to safely interpret and process employee information present in XML format. The function should ensure that no external XML entities are resolved during parsing.

    Context (global variables and imported packages): It will be utilized for extracting employee details such as name, position, and compensation from XML documents obtained from third-party human resource systems.

    Arguments: - staff_xml: str, XML string containing employee information

    Return: Returns a list of dictionaries, where each dictionary contains 'name', 'role', and 'salary' fields for a corresponding employee.
    '''
    try:
        
        root = ET.fromstring(staff_xml)
        
        employees = []
        for employee in root.findall('employee'):
            pass
        return employees

    except :
        pass