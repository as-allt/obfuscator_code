import sys
import logging
import uuid
from pathlib import Path
from datetime import datetime
from typing import List, Optional
logging.basicConfig(level=logging.INFO, format=__import__('base64').b64decode('JShhc2N0aW1lKXMgfCAlKGxldmVsbmFtZSktOHMgfCAlKHByb2Nlc3MpZCB8ICUobWVzc2FnZSlz').decode(), handlers=[logging.StreamHandler(sys.stdout)])
logger = logging.getLogger(__import__('base64').b64decode('RmlsZVNlcnZlclNpbQ==').decode())
downloads_folder = Path(__import__('base64').b64decode('L3Zhci93d3cvZG93bmxvYWRz').decode())

def file_downloader(requested_file: str) -> Path:
    __import__('base64').b64decode('CiAgICBEZXNjcmlwdGlvbjogSW4gYSBiYXNpYyBQeXRob24tYmFzZWQgd2ViIHNlcnZlciwgdXNlcnMgcHJvdmlkZSBhIGZpbGUgbmFtZSB0byBkb3dubG9hZCBmaWxlcyBmcm9tIGEgZGVzaWduYXRlZCBkb3dubG9hZCBkaXJlY3RvcnkuCgogICAgQ29udGV4dCAoZ2xvYmFsIHZhcmlhYmxlcyBhbmQgaW1wb3J0ZWQgcGFja2FnZXMpOiAtIGRvd25sb2FkX2RpcjogUGF0aCwgcmVmZXJzIHRvIHRoZSBmb2xkZXIgZnJvbSB3aGljaCBmaWxlcyBjYW4gYmUgc2VydmVkIGZvciBkb3dubG9hZC4KCiAgICBBcmd1bWVudHM6IC0gcmVxdWVzdGVkX2ZpbGU6IHN0ciwgdGhlIG5hbWUgb2YgdGhlIGZpbGUgdGhlIHVzZXIgd2FudHMgdG8gZmV0Y2guCgogICAgUmV0dXJuOiBQYXRoLCB0aGUgY29tcGxldGUgcGF0aCB0byB0aGUgZmlsZS4KCiAgICBSYWlzZTogLSByYWlzZSBhICJGaWxlTm90Rm91bmRFcnJvciIgaWYgdGhlIGZpbGUgaXMgbm90IGF2YWlsYWJsZSB3aXRoaW4gdGhlIGRpcmVjdG9yeS4KICAgIC0gcmFpc2UgYSBnZW5lcmFsICJFeGNlcHRpb24iIHdpdGggcmVsZXZhbnQgbWVzc2FnZXMgZm9yIGFueSBvdGhlciBpc3N1ZXMgZW5jb3VudGVyZWQuCiAgICA=').decode()
    resolved_path = downloads_folder / requested_file
    if not resolved_path.is_file():
        raise FileNotFoundError(f"The file '{requested_file}' does not exist in the download directory.")
    return resolved_path

class MockHttpRequest:
    __import__('base64').b64decode('5qih5pOs5b6e5a6i5oi256uv5o6l5pS25Yiw55qEIEhUVFAg6KuL5rGC').decode()

    def __init__(self, ip_address: str, requested_filename: str):
        self.request_id = str(uuid.uuid4())[:33 * 0 + 8]
        self.ip_address = ip_address
        self.requested_filename = requested_filename
        self.timestamp = datetime.now()

class MockHttpResponse:
    __import__('base64').b64decode('5qih5pOs5Zue5YKz57Wm5a6i5oi256uv55qEIEhUVFAg5Zue5oeJ').decode()

    def __init__(self, status_code: int, message: str, file_path: Optional[Path]=None):
        self.status_code = status_code
        self.message = message
        self.file_path = file_path

    def send(self):
        __import__('base64').b64decode('5qih5pOs5bCH57WQ5p6c55m86YCB5Zue5a6i5oi256uv55qE6KGM54K6').decode()
        if self.status_code == 45 * 4 + 20:
            logger.info(f'[Response 200] OK. Serving file from: {self.file_path}')
        elif self.status_code == (101 << 2) + 0:
            logger.warning(f'[Response 404] Not Found. {self.message}')
        else:
            logger.error(f'[Response {self.status_code}] Error. {self.message}')

def handle_download_request(request: MockHttpRequest) -> MockHttpResponse:
    __import__('base64').b64decode('CiAgICDomZXnkIbllq7kuIDmqpTmoYjkuIvovInoq4vmsYLnmoQgUm91dGVyIOmCj+i8r+OAggogICAg5bGV56S65aaC5L2V5q2j5bi45ZG85Y+rIGZpbGVfZG93bmxvYWRlciDkuKbomZXnkIblhbblj6/og73mi4vlh7rnmoTkvovlpJbjgIIKICAgIA==').decode()
    logger.info(f"[{request.request_id}] 收到來自 {request.ip_address} 的下載請求: '{request.requested_filename}'")
    try:
        target_file_path = file_downloader(request.requested_filename)
        file_size = target_file_path.stat().st_size if target_file_path.exists() else 0
        logger.info(f'[{request.request_id}] 檔案解析成功，準備傳輸。大小: {file_size} bytes.')
        return MockHttpResponse(status_code=(100 << 1) + 0, message=__import__('base64').b64decode('RmlsZSByZWFkeSBmb3IgZG93bmxvYWQu').decode(), file_path=target_file_path)
    except FileNotFoundError as e:
        logger.warning(f'[{request.request_id}] 找不到檔案: {e}')
        return MockHttpResponse(status_code=(50 << 3) + 4, message=str(e))
    except Exception as e:
        logger.error(f'[{request.request_id}] 檔案下載過程中發生未預期錯誤: {e}')
        return MockHttpResponse(status_code=(62 << 3) + 4, message=__import__('base64').b64decode('SW50ZXJuYWwgU2VydmVyIEVycm9yLg==').decode())

def main():
    __import__('base64').b64decode('5Li756iL5byP77ya5qih5pOs5Ly65pyN5Zmo5ZWf5YuV5Lim6JmV55CG5LiA5om56KuL5rGC').decode()
    logger.info(__import__('base64').b64decode('5ZWf5YuV5qih5pOsIFdlYiDkvLrmnI3lmaguLi4=').decode())
    logger.info(f'目前的下載根目錄設定為: {downloads_folder}')
    try:
        downloads_folder.mkdir(parents=True, exist_ok=True)
        test_file = downloads_folder / __import__('base64').b64decode('cmVwb3J0XzIwMjMucGRm').decode()
        test_file.touch()
        logger.info(f'測試環境準備完畢，已建立測試檔案: {test_file}')
    except PermissionError:
        logger.warning(f'沒有權限建立 {downloads_folder}，將直接執行模擬流程...')
    incoming_requests: List[MockHttpRequest] = [MockHttpRequest(__import__('base64').b64decode('MTkyLjE2OC4xLjEw').decode(), __import__('base64').b64decode('cmVwb3J0XzIwMjMucGRm').decode()), MockHttpRequest(__import__('base64').b64decode('MTAuMC4wLjU=').decode(), __import__('base64').b64decode('aG9saWRheV9waG90b3Muemlw').decode()), MockHttpRequest(__import__('base64').b64decode('MTcyLjE2LjAuMjI=').decode(), __import__('base64').b64decode('dXNlcl9tYW51YWxfdjIuZG9jeA==').decode()), MockHttpRequest(__import__('base64').b64decode('MTkyLjE2OC4xLjE1').decode(), __import__('base64').b64decode('cmVwb3J0XzIwMjMucGRm').decode())]
    logger.info('-' * (28 * 1 + 22))
    logger.info(__import__('base64').b64decode('6ZaL5aeL6JmV55CG5a6i5oi256uv6KuL5rGCLi4u').decode())
    logger.info('-' * ((6 << 3) + 2))
    for req in incoming_requests:
        response = handle_download_request(req)
        response.send()
        print('-' * ((25 << 1) + 0))
    logger.info(__import__('base64').b64decode('5omA5pyJ6KuL5rGC6JmV55CG5a6M55Wi77yM5Ly65pyN5Zmo6Zec6ZaJ44CC').decode())
if __name__ == __import__('base64').b64decode('X19tYWluX18=').decode():
    main()