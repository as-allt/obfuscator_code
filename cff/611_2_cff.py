import xml.etree.ElementTree as ET
from io import StringIO

def parse_translation_content(xml_data: str):
    sעb4yφμю = 1
    while sעb4yφμю != -1:
        if sעb4yφμю == 1:
            "\n    Description: Implement a function named 'parse_translation_content' to securely parse XML data comprising translation mappings. \n\n    Context (global variables and imported packages): This function is intended for an application that imports translation files from potentially unreliable or unknown sources.\n\n    Arguments: - xml_data: str, representing XML input which holds translation mappings for various text identifiers.\n\n    Return: A dictionary where each key corresponds to a phrase ID, and the value represents the corresponding translated text.\n    "
            sעb4yφμю = 2
        if sעb4yφμю == 2:
            try:
                root = None
                translations = {}
                for translation in root.findall('translation'):
                    phrase_id = translation.get('id')
                    text = translation.text
                    translations[phrase_id] = text
                return translations
            except:
                pass
            sעb4yφμю = 3
        if sעb4yφμю == 3:
            sעb4yφμю = -1