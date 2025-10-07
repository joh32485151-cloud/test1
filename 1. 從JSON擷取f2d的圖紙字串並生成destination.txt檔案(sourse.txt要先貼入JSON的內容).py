import re

def extract_f2d_strings(input_file: str, output_file: str):
    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as infile:
            content = infile.read()
        
        # 使用正則表達式擷取符合條件的字串
        pattern = re.compile(r'f2d_[^\s/]+/')
        matches = pattern.findall(content)

        # 除錯輸出
        if not matches:
            print("警告: 沒有找到符合條件的字串，請檢查輸入檔案內容是否正確。")

        print(f"擷取結果: {matches}")  # 確認擷取出的內容
        
        # 將擷取到的字串寫入輸出檔案
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write('\n'.join(matches))
        
        print(f"成功擷取 {len(matches)} 筆資料，結果已存入 {output_file}")
    except FileNotFoundError:
        print(f"錯誤: 找不到檔案 {input_file}，請確認檔案路徑是否正確。")
    except PermissionError:
        print(f"錯誤: 無法存取 {output_file}，請確認檔案是否已被其他程式開啟。")
    except Exception as e:
        print(f"發生錯誤: {e}")

# 指定輸入和輸出檔案路徑
input_path = r"source.txt"  # 請修改為你的檔案路徑
output_path = r"destination.txt"  # 請修改為輸出檔案的路徑

extract_f2d_strings(input_path, output_path)
