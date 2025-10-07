import re
from collections import Counter

def extract_common_keywords(lines, min_count=3):
    text = ''.join(lines)
    chinese_words = re.findall(r'[\u4e00-\u9fff]{2,}', text)
    counter = Counter(chinese_words)
    return [word for word, count in counter.items() if count >= min_count]

def process_text_file_with_auto_filter(input_file: str, output_file: str):
    try:
        with open(input_file, 'r', encoding='utf-8-sig', errors='ignore') as infile:
            lines = infile.readlines()

        # 萃取常見中文關鍵字
        keywords = extract_common_keywords(lines)

        # 產生下拉選單項目
        options_html = '\n'.join([f'<option value="{kw}">{kw}</option>' for kw in keywords])

        # 建立 <ul> 清單
        ul_lines = ["<ul id=\"drawingList\">"]
        for line in lines:
            line = line.strip()
            if line.endswith('/'):
                line = line[:-1]
            display_name = line.split('/')[-1]
            modified_url = f"{line}/index-online.html"
            ul_lines.append(f'    <li><a href="{modified_url}" target="_blank">{display_name}</a></li>')
        ul_lines.append("</ul>")
        ul_content = '\n'.join(ul_lines)

        # 組合 HTML
        full_html = f"""<!DOCTYPE html>
<html lang=\"zh-Hant\">
<head>
    <meta charset=\"UTF-8\">
    <title>圖紙清單</title>
    <style>
        body {{
            font-family: sans-serif;
            padding: 20px;
        }}
        #controls {{
            margin-bottom: 20px;
        }}
        #controls input, #controls select {{
            margin-right: 10px;
            padding: 5px;
            font-size: 1em;
        }}
        ul li {{
            margin-bottom: 5px;
        }}
    </style>
</head>
<body>

<div id=\"controls\">
    <input type=\"text\" id=\"searchInput\" placeholder=\"輸入關鍵字搜尋...\">
    <select id=\"categoryFilter\">
        <option value=\"\">-- 類型篩選 --</option>
        {options_html}
    </select>
</div>

{ul_content}

<script>
    const drawingList = document.getElementById('drawingList');
    const originalItems = [...drawingList.querySelectorAll('li')];

    document.getElementById('searchInput').addEventListener('input', filterList);
    document.getElementById('categoryFilter').addEventListener('change', filterList);

    function filterList() {{
        const keyword = document.getElementById('searchInput').value.toLowerCase();
        const category = document.getElementById('categoryFilter').value;

        drawingList.innerHTML = '';

        originalItems.forEach(item => {{
            const text = item.textContent.toLowerCase();
            const matchKeyword = !keyword || text.includes(keyword);
            const matchCategory = !category || text.includes(category.toLowerCase());

            if (matchKeyword && matchCategory) {{
                drawingList.appendChild(item);
            }}
        }});
    }}
</script>

</body>
</html>
"""

        with open(output_file, 'w', encoding='utf-8-sig', errors='ignore') as outfile:
            outfile.write(full_html)

        print(f"✅ HTML 自動分類生成完成：{output_file}")
    except Exception as e:
        print(f"❌ 發生錯誤: {e}")

# 使用範例
if __name__ == "__main__":
    input_path = "destination.txt"
    output_path = "drawinglist.html"
    process_text_file_with_auto_filter(input_path, output_path)
