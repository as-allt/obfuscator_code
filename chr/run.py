import subprocess
import os

# 圖片中列出的所有資料夾編號
folders = [
    "022", "074", "077", "078", "079", "094", "095", "120",
    "200", "281", "295", "327", "338", "347", "352", "367",
    "400", "502", "601", "611", "732", "770", "862", "863",
    "915", "918", "1333"
]

# 迴圈遍歷每個資料夾
for folder in folders:
    # 每個資料夾有 _1 和 _2 兩個檔案
    for i in range(1, 3):
        input_file = f"../{folder}/{folder}_{i}_code.py"
        output_file = f"{folder}_{i}_b64.py"
        
        # 檢查輸入檔案是否存在（避免因為缺檔案導致腳本報錯中斷）
        if not os.path.exists(input_file):
            print(f"⚠️ 找不到檔案，已跳過: {input_file}")
            continue

        # 構建要執行的指令
        command = [
            "python3", "../snailobfuscator.py",
            "-i", input_file,
            "-o", output_file,
            "--preset", "chr"
        ]

        print(f"🚀 正在執行: {' '.join(command)}")

        # 執行指令
        try:
            subprocess.run(command, check=True)
            print(f"✅ 成功產出: {output_file}\n")
        except subprocess.CalledProcessError as e:
            print(f"❌ 處理失敗: {input_file}\n")
            
print("🎉 所有任務執行完畢！")