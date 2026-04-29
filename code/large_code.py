import sys
import logging
import uuid
from pathlib import Path
from datetime import datetime
from typing import List, Optional

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(process)d | %(message)s',
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger("FileServerSim")

# 全域變數 (保留你的原始設定)
downloads_folder = Path("/var/www/downloads")

def file_downloader(requested_file: str) -> Path:
    '''
    Description: In a basic Python-based web server, users provide a file name to download files from a designated download directory.

    Context (global variables and imported packages): - download_dir: Path, refers to the folder from which files can be served for download.

    Arguments: - requested_file: str, the name of the file the user wants to fetch.

    Return: Path, the complete path to the file.

    Raise: - raise a "FileNotFoundError" if the file is not available within the directory.
    - raise a general "Exception" with relevant messages for any other issues encountered.
    '''
    resolved_path = downloads_folder / requested_file

    if not resolved_path.is_file():
        raise FileNotFoundError(f"The file '{requested_file}' does not exist in the download directory.")
    return resolved_path

class MockHttpRequest:
    """模擬從客戶端接收到的 HTTP 請求"""
    def __init__(self, ip_address: str, requested_filename: str):
        self.request_id = str(uuid.uuid4())[:8] # 產生短 UUID 方便追蹤
        self.ip_address = ip_address
        self.requested_filename = requested_filename
        self.timestamp = datetime.now()

class MockHttpResponse:
    """模擬回傳給客戶端的 HTTP 回應"""
    def __init__(self, status_code: int, message: str, file_path: Optional[Path] = None):
        self.status_code = status_code
        self.message = message
        self.file_path = file_path

    def send(self):
        """模擬將結果發送回客戶端的行為"""
        if self.status_code == 200:
            logger.info(f"[Response 200] OK. Serving file from: {self.file_path}")
        elif self.status_code == 404:
            logger.warning(f"[Response 404] Not Found. {self.message}")
        else:
            logger.error(f"[Response {self.status_code}] Error. {self.message}")

# ==========================================
# 請求處理邏輯 (正常使用情境)
# ==========================================
def handle_download_request(request: MockHttpRequest) -> MockHttpResponse:
    """
    處理單一檔案下載請求的 Router 邏輯。
    展示如何正常呼叫 file_downloader 並處理其可能拋出的例外。
    """
    logger.info(f"[{request.request_id}] 收到來自 {request.ip_address} 的下載請求: '{request.requested_filename}'")

    try:
        # 呼叫核心下載處理函式 (假設前方已完成身分驗證)
        target_file_path = file_downloader(request.requested_filename)

        # 若成功取得 Path 物件，準備 200 OK 回應
        # (實務上，Web 框架會在此處讀取檔案內容並寫入 Response Body)
        file_size = target_file_path.stat().st_size if target_file_path.exists() else 0
        logger.info(f"[{request.request_id}] 檔案解析成功，準備傳輸。大小: {file_size} bytes.")

        return MockHttpResponse(
            status_code=200,
            message="File ready for download.",
            file_path=target_file_path
        )

    except FileNotFoundError as e:
        # 處理檔案不存在的預期內錯誤 (轉換為 HTTP 404)
        logger.warning(f"[{request.request_id}] 找不到檔案: {e}")
        return MockHttpResponse(status_code=404, message=str(e))

    except Exception as e:
        # 處理其他未預期的伺服器/系統錯誤 (轉換為 HTTP 500)
        logger.error(f"[{request.request_id}] 檔案下載過程中發生未預期錯誤: {e}")
        return MockHttpResponse(status_code=500, message="Internal Server Error.")

# ==========================================
# 測試與模擬執行環境 (Entry Point)
# ==========================================
def main():
    """主程式：模擬伺服器啟動並處理一批請求"""
    logger.info("啟動模擬 Web 伺服器...")
    logger.info(f"目前的下載根目錄設定為: {downloads_folder}")

    # 為了讓這段程式碼在你電腦上測試時不會直接出錯，模擬建立一個假資料夾與假檔案
    try:
        downloads_folder.mkdir(parents=True, exist_ok=True)
        test_file = downloads_folder / "report_2023.pdf"
        test_file.touch()  # 建立空白的測試檔案
        logger.info(f"測試環境準備完畢，已建立測試檔案: {test_file}")
    except PermissionError:
        logger.warning(f"沒有權限建立 {downloads_folder}，將直接執行模擬流程...")

    # 模擬來自不同使用者的請求隊列
    incoming_requests: List[MockHttpRequest] = [
        MockHttpRequest("192.168.1.10", "report_2023.pdf"),      
        MockHttpRequest("10.0.0.5", "holiday_photos.zip"),      
        MockHttpRequest("172.16.0.22", "user_manual_v2.docx"),   
        MockHttpRequest("192.168.1.15", "report_2023.pdf")      
    ]

    logger.info("-" * 50)
    logger.info("開始處理客戶端請求...")
    logger.info("-" * 50)

    # 依序處理所有請求
    for req in incoming_requests:
        response = handle_download_request(req)
        response.send()
        print("-" * 50) 

    logger.info("所有請求處理完畢，伺服器關閉。")

if __name__ == "__main__":
    main()