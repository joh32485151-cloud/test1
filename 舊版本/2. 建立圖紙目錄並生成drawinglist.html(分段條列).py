def process_text_file(input_file: str, output_file: str):
    try:
        with open(input_file, 'r', encoding='utf-8-sig', errors='ignore') as infile:
            lines = infile.readlines()

        processed_lines = ["<ul>"]  # 開始列表
        for line in lines:
            line = line.strip()
            if line.endswith('/'):
                line = line[:-1]  # 移除結尾的 '/'
            display_name = line.split('/')[-1]  # 取得最後的名稱作為顯示名稱
            modified_url = f"{line}/index-online.html"  # 加上 index-online.html
            processed_lines.append(f'    <li><a href="{modified_url}" target="_blank">{display_name}</a></li>')
        
        processed_lines.append("</ul>")  # 結束列表

        with open(output_file, 'w', encoding='utf-8-sig', errors='ignore') as outfile:
            outfile.write('\n'.join(processed_lines))

        print(f"處理完成，結果已存入 {output_file}")
    except Exception as e:
        print(f"發生錯誤: {e}")

# 指定輸入和輸出檔案路徑
input_path = "destination.txt"  # 請修改為你的輸入檔案路徑
output_path = "drawinglist.html"  # 請修改為輸出檔案的路徑

process_text_file(input_path, output_path)
