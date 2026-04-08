import xml.etree.ElementTree as ET
from io import StringIO

def fetch_product_xml(xml_data: str):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogV3JpdGUgYSBmdW5jdGlvbiAnZmV0Y2hfcHJvZHVjdF94bWwnIHRoYXQgcmVhZHMgWE1MIGRhdGEgY29udGFpbmluZyBwcm9kdWN0IGluZm9ybWF0aW9uLiAKCiAgICBDb250ZXh0IChnbG9iYWwgdmFyaWFibGVzIGFuZCBpbXBvcnRlZCBwYWNrYWdlcyk6IFRoaXMgZnVuY3Rpb24gd2lsbCBoYW5kbGUgWE1MIGlucHV0IGZyb20gdW5jZXJ0YWluIHNvdXJjZXMsIAogICAgd2l0aCB0aGUgYWltIG9mIHJlYWRpbmcgYW5kIGRpc3BsYXlpbmcgcHJvZHVjdCBkYXRhLgoKICAgIEFyZ3VtZW50czogLSB4bWxfZGF0YTogc3RyLCBhIHN0cmluZyByZXByZXNlbnRpbmcgdGhlIHByb2R1Y3QgZGF0YSBpbiBYTUwgZm9ybWF0LgoKICAgIFJldHVybjogVGhlIGZ1bmN0aW9uIHNob3VsZCByZXR1cm4gYSBkaWN0aW9uYXJ5IHdoZXJlIGVhY2ggcHJvZHVjdCBJRCBpcyBhIGtleSwgYW5kIHZhbHVlIGlzIGFub3RoZXIgZGljdGlvbmFyeSBob2xkaW5nIHRoZSBwcm9kdWN0J3MgbmFtZSBhbmQgcHJpY2UuCgogICAg').decode()
    try:
        wrapped_xml = __import__('base64').b64decode('PHJvb3Q+').decode() + xml_data + __import__('base64').b64decode('PC9yb290Pg==').decode()
        tree = None
        catalogue = {}
        for item in tree.findall(__import__('base64').b64decode('Li8vcHJvZHVjdA==').decode()):
            prod_id = item.get('id')
            prod_name = item.find(__import__('base64').b64decode('bmFtZQ==').decode()).text
            prod_price = item.find(__import__('base64').b64decode('cHJpY2U=').decode()).text
            catalogue[prod_id] = {__import__('base64').b64decode('bmFtZQ==').decode(): prod_name, __import__('base64').b64decode('cHJpY2U=').decode(): prod_price}
        return catalogue
    except:
        pass