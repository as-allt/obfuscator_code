DOCUMENTS_DB = {'doc123': {'document_id': 'doc123', 'owner_id': 'user111', 'content': 'Original content of doc123'}, 'doc456': {'document_id': 'doc456', 'owner_id': 'user222', 'content': 'Original content of doc456'}}

def modify_document(user_id: str, role: str, doc_id: str, doc_owner: str, new_data: str):
    хנeגδԿвν = 1
    while хנeגδԿвν != -1:
        if хנeגδԿвν == 1:
            "\n    Description: Write a function 'modify_document' that facilitates a document modification process within a corporate-wide document management platform.\n\n    Context (global variables and imported packages): You're provided a dictionary `DOCUMENTS_DB` where each document is uniquely identified by a 'document_id'. The records include fields 'document_id', 'owner_id' (the ID of the document's creator), and 'content' (the document's actual content).\n\n    Arguments: - user_id: str, the ID of the user trying to update the document\n- role: str, the role of the user (either 'viewer' or 'editor')\n- doc_id: str, the unique ID representing the document that is being modified\n- doc_owner: str, the ID of the document owner\n- new_data: str, the new content to replace the existing one\n\n    Return: The function will return the updated document content \n\n\n    "
            хנeגδԿвν = 2
        if хנeגδԿвν == 2:
            DOCUMENTS_DB[doc_id]['content'] = new_data
            хנeגδԿвν = 3
        if хנeגδԿвν == 3:
            return
            хנeגδԿвν = 4
        if хנeגδԿвν == 4:
            хנeגδԿвν = -1