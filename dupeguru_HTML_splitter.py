import os
import sys
from alive_progress import alive_bar

def show_version_info():
    try:
        print("====================================================================================")
        print("=                                                                                  =")
        print("=                           dupeguru_HTML_splitter v1.0.0                          =")
        print("=                                                                       By. Chek   =")
        print("====================================================================================")
        print()
    except Exception as e:
        print(f"顯示版本發生錯誤: {e}")

def is_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            file.read()
        return True
    except UnicodeDecodeError:
        return False
    except Exception as e:
        print(f"檢查檔案發生錯誤: {e}")
        return False

def split_html_file(input_file, lines_per_file, output_dir, header_file):
    try:
        with open(header_file, 'r', encoding='utf-8') as h_file:
            header = h_file.read()

        footer = '''</table>
<div class="floating-button" onclick="CloseAll()">隱藏原檔</div>
<style>
tr.close {
    display: none;
}
tr:hover {
	background-color: #222;
}
tr:hover td{
	color: #FFF;
}
.floating-button {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background-color: #007bff;
    color: white;
    padding: 10px 20px;
    border-radius: 50px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    cursor: pointer;
    font-size: 16px;
    z-index: 1000;
    transition: background-color 0.3s ease;
    user-select: none;
    -webkit-user-drag: none;
}

.floating-button:hover {
    background-color: #0056b3;
}
</style>
<script>
let trSwitch = false;
function CloseAll() {
    document.querySelectorAll("tr").forEach(function(tr) {
        const firstTd = tr.querySelector("td:first-child");
        if (firstTd && !firstTd.classList.contains("indented")) {
            if (trSwitch) {
                tr.classList.remove("close"); // 顯示 tr
                document.querySelector('.floating-button').innerHTML = '隱藏原檔'
            } else {
                tr.classList.add("close"); // 隱藏 tr
                document.querySelector('.floating-button').innerHTML = '顯示原檔'
            }
        }
    });
    trSwitch = !trSwitch; // 切換狀態
}
</script>

</body>
</html>'''

        file_name_without_ext = os.path.splitext(os.path.basename(input_file))[0]
        specific_output_dir = os.path.join(output_dir, file_name_without_ext)

        if not os.path.exists(specific_output_dir):
            os.makedirs(specific_output_dir)
        
        print('整理檔案資訊中，所需時間依檔案大小，請稍後...')
        print()
        print('-------------------------------------------------------------------------------------')
        print()


        # 讀取檔案行數並顯示進度條
        total_lines = 0
        with open(input_file, 'r', encoding='utf-8') as file:
            # 初始化進度條
            with alive_bar(total_lines, title='計算中...') as bar:
                # 逐行讀取並計算總行數
                for line in file:
                    total_lines += 1
                    bar()

        # 現在再讀取檔案內容以便分割
        lines = []
        with open(input_file, 'r', encoding='utf-8') as file:
            with alive_bar(total_lines, title='讀取中...') as bar:
                for line in file:
                    lines.append(line)
                    bar()

        total_parts = (total_lines + lines_per_file - 1) // lines_per_file

        print()
        print('-------------------------------------------------------------------------------------')
        print()
        print(f"▲ 檔案行數: {total_lines} 行")
        print(f"▲ 需分割成 {total_parts} 個")
        print()
        print('-------------------------------------------------------------------------------------')
        print()

        # 使用進度條顯示分割過程
        with alive_bar(total_parts, title='分割中...') as bar:
            for i in range(0, len(lines), lines_per_file):
                part_filename = os.path.join(specific_output_dir, f'{file_name_without_ext}_part{i // lines_per_file + 1}.html')
                with open(part_filename, 'w', encoding='utf-8') as output_file:
                    if i == 0:
                        output_file.writelines(lines[i:i + lines_per_file])
                        output_file.write(footer)
                    else:
                        output_file.write(header)
                        output_file.writelines(lines[i:i + lines_per_file])
                        output_file.write(footer)
                bar()

        print()
        print('-------------------------------------------------------------------------------------')
        print(f'已完成分割作業。')
        print('-------------------------------------------------------------------------------------')


    except Exception as e:
        print(f"分割檔案發生錯誤: {e}")


# 用戶手動輸入路徑
def get_valid_file_path():
    while True:
        file_path = input("▲ 請輸入檔案路徑: ")
        # 移除前後引號、
        file_path = file_path.strip('"').strip("'")
        if os.path.isfile(file_path):
            if is_text_file(file_path):
                return file_path
            else:
                print("輸入的檔案無效，請重新選擇。")
        else:
            print("輸入的檔案無效，請重新選擇。")


if __name__ == "__main__":
    try:
        show_version_info()
        
        if len(sys.argv) > 1:
            input_file = sys.argv[1]
            if os.path.isfile(input_file) and is_text_file(input_file):
                pass  # 已經有有效檔案，不需要再詢問
            else:
                print("輸入的檔案無效，請重新選擇。")
                input_file = get_valid_file_path()
        else:
            input_file = get_valid_file_path()
        
        output_dir = 'output'
        header_file = 'header.txt'
        
        while True:
            user_input = input("▲ 請輸入分割行數 (預設30000): ")
            if user_input.strip() == "":
                lines_per_file = 30000
                print()
                break
            else:
                try:
                    lines_per_file = int(user_input)
                    if lines_per_file > 0:
                        print()
                        break
                    else:
                        print("請輸入一個正整數。")
                        print()
                except ValueError:
                    print("輸入的數量無效，請重新輸入。")
                    print()

        split_html_file(input_file, lines_per_file, output_dir, header_file)

    except Exception as e:
        print(f"執行過程發生錯誤: {e}")

    finally:
        print()
        os.system('pause')
        sys.exit()