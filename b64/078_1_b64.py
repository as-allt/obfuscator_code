import os
import logging
import subprocess
logger = logging.getLogger(__name__)

def convert_markdown_to_pdf_uri(src_markdown_path: str, dest_pdf_path: str):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogVGhpcyBmdW5jdGlvbiBwZXJmb3JtcyB0aGUgdGFzayBvZiB0cmFuc2Zvcm1pbmcgYSBtYXJrZG93biBmaWxlIGludG8gYSBQREYgYnkgdXNpbmcgYW4gZXh0ZXJuYWwgdG9vbC4gVGhlIGBwYW5kb2NgIGNvbW1hbmQtbGluZSB1dGlsaXR5IGlzIGVtcGxveWVkIHRvIGhhbmRsZSB0aGlzIGNvbnZlcnNpb24uCgogICAgQ29udGV4dCAoZ2xvYmFsIHZhcmlhYmxlcyBhbmQgaW1wb3J0ZWQgcGFja2FnZXMpOiAtIGxvZ2dlcjogYW4gb2JqZWN0IGZyb20gdGhlIGBsb2dnaW5nLkxvZ2dlcmAgY2xhc3MgdGhhdCBmYWNpbGl0YXRlcyBkZWJ1ZyBhbmQgaW5mbyBsb2dnaW5nLgotIGxvZ2dpbmc6IHRoZSBidWlsdC1pbiBQeXRob24gbG9nZ2luZyBtb2R1bGUgdG8gcmVjb3JkIG1lc3NhZ2VzLgotIHN1YnByb2Nlc3M6IGEgbW9kdWxlIHVzZWQgaW4gUHl0aG9uIHRvIHJ1biBleHRlcm5hbCBjb21tYW5kcyBhbmQgbWFuYWdlIGlucHV0L291dHB1dC9lcnJvciBzdHJlYW1zLgoKICAgIEFyZ3VtZW50czogLSBzcmNfbWFya2Rvd25fcGF0aCAoc3RyKTogVGhlIGZpbGVwYXRoIG9mIHRoZSBtYXJrZG93biBkb2N1bWVudCB0byBiZSB0cmFuc2xhdGVkLgotIGRlc3RfcGRmX3BhdGggKHN0cik6IFRoZSB0YXJnZXRlZCBmaWxlcGF0aCB0byBzdG9yZSB0aGUgcmVzdWx0aW5nIFBERiBmaWxlLgoKICAgIFJldHVybjogTm9uZQoKICAgIA==').decode()
    __import__('base64').b64decode('Q29udmVydHMgYSBtYXJrZG93biBmaWxlIHRvIGEgUERGIHVzaW5nIHBhbmRvYy4=').decode()
    logger.info(__import__('base64').b64decode('Q29udmVydGluZyBtYXJrZG93biBmaWxlIHRvIFBERi4uLg==').decode())
    if not os.path.exists(src_markdown_path):
        logger.error(__import__('base64').b64decode('TWFya2Rvd24gZmlsZSBub3QgZm91bmQ6ICVz').decode(), src_markdown_path)
        raise FileNotFoundError(f'Markdown file not found: {src_markdown_path}')
    if not src_markdown_path.endswith(__import__('base64').b64decode('Lm1k').decode()):
        logger.error(__import__('base64').b64decode('SW52YWxpZCBmaWxlIHR5cGU6ICVz').decode(), src_markdown_path)
        return