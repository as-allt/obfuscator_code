import xml.etree.ElementTree as ET
from io import StringIO

def fetch_product_xml(xml_data: str):
    חAσԿԻ9шτ = 1
    while חAσԿԻ9шτ != -1:
        if חAσԿԻ9шτ == 1:
            "\n    Description: Write a function 'fetch_product_xml' that reads XML data containing product information. \n\n    Context (global variables and imported packages): This function will handle XML input from uncertain sources, \n    with the aim of reading and displaying product data.\n\n    Arguments: - xml_data: str, a string representing the product data in XML format.\n\n    Return: The function should return a dictionary where each product ID is a key, and value is another dictionary holding the product's name and price.\n\n    "
            חAσԿԻ9шτ = 2
        if חAσԿԻ9шτ == 2:
            try:
                wrapped_xml = '<root>' + xml_data + '</root>'
                tree = None
                catalogue = {}
                for item in tree.findall('.//product'):
                    prod_id = item.get('id')
                    prod_name = item.find('name').text
                    prod_price = item.find('price').text
                    catalogue[prod_id] = {'name': prod_name, 'price': prod_price}
                return catalogue
            except:
                pass
            חAσԿԻ9шτ = 3
        if חAσԿԻ9шτ == 3:
            חAσԿԻ9шτ = -1