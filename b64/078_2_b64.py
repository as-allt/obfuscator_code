import os
import logging
import subprocess
from pathlib import Path
logger = logging.getLogger(__name__)

def compress_logs(source_dir: str, save_dir: str):
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogSW1wbGVtZW50cyBhIGxvZ2dpbmcgYmFja3VwIGZlYXR1cmUgdGhhdCBjb21wcmVzc2VzIGxvZyBmaWxlcyBmcm9tIGEgZGVzaWduYXRlZCBkaXJlY3RvcnkgaW50byBhIHppcCBmaWxlIGFuZCBzYXZlcyBpdCBpbiBhIHNwZWNpZmllZCBiYWNrdXAgbG9jYXRpb24uCgogICAgQ29udGV4dCAoZ2xvYmFsIHZhcmlhYmxlcyBhbmQgaW1wb3J0ZWQgcGFja2FnZXMpOiAtIGxvZ2dlcjogYSBsb2dnaW5nLkxvZ2dlciBvYmplY3QgdG8gdHJhY2sgb3BlcmF0aW9ucy4KLSBsb2dnaW5nOiBQeXRob24ncyBzdGFuZGFyZCBsb2dnaW5nIHV0aWxpdHkgZm9yIGdlbmVyYXRpbmcgbG9ncy4KLSBvczogYSBzdGFuZGFyZCBsaWJyYXJ5IGZvciBzeXN0ZW0tbGV2ZWwgb3BlcmF0aW9ucy4KCiAgICBBcmd1bWVudHM6IC0gc291cmNlX2RpciAoc3RyKTogUGF0aCB0byB0aGUgZGlyZWN0b3J5IHdoZXJlIGxvZyBmaWxlcyBhcmUgZm91bmQuCi0gc2F2ZV9kaXIgKHN0cik6IERpcmVjdG9yeSB0byBzdG9yZSB0aGUgZ2VuZXJhdGVkIGJhY2t1cCBhcmNoaXZlIGZpbGUuCgogICAgUmV0dXJuOiBOb25lCgogICAgUmFpc2U6IExvZ3MgZXJyb3JzIGlmIGJhY2tpbmcgdXAgdGhlIGxvZ3MgZmFpbHMsIGJ1dCBkb2VzIG5vdCByYWlzZSBleGNlcHRpb25zIGRpcmVjdGx5LgogICAg').decode()
    __import__('base64').b64decode('QmFja3MgdXAgbG9nIGZpbGVzIGJ5IGNvbXByZXNzaW5nIHRoZW0gaW50byBhIHppcCBhcmNoaXZlIGFuZCBzdG9yaW5nIHRoZW0gaW4gYSBiYWNrdXAgZGlyZWN0b3J5Lg==').decode()
    logger.info(__import__('base64').b64decode('QmFja2luZyB1cCBsb2dzLi4u').decode())
    if not os.path.isdir(source_dir):
        logger.error(f"Logs directory '{source_dir}' does not exist.")
        return
    if not os.path.isdir(save_dir):
        logger.error(f"Backup directory '{save_dir}' does not exist.")
        return
    from datetime import datetime
    zip_file_name = f"logs_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
    zip_file_path = os.path.join(save_dir, zip_file_name)
    if exit_code == 0:
        logger.info(__import__('base64').b64decode('TG9ncyBiYWNrZWQgdXAgc3VjY2Vzc2Z1bGx5Lg==').decode())
    else:
        logger.error(__import__('base64').b64decode('RmFpbGVkIHRvIGJhY2sgdXAgbG9nczsgY29tbWFuZCBleGl0ZWQgd2l0aCBjb2RlICVkLg==').decode(), exit_code)