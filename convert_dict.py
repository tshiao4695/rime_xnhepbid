import os
import sys
from datetime import datetime
from flypy import tofly

with open("info.yaml", 'r', encoding='utf-8') as f:
    extra_content = f.read()

def process_encoding(codes, method):
    if method == 'tofly':
        return tofly("".join(codes))

def gen_dict(input_file_path, output_file_path=None, encoding_method='tofly', separator=' '):
    if output_file_path is None:
        base_name, ext = os.path.splitext(input_file_path)
        output_file_path = f"{base_name}_gen{ext}"

    base_name = os.path.splitext(os.path.basename(output_file_path))[0].replace(".dict", "")
    
    fuma = set()
    HEADER = f'''---
name: {base_name}
version: "{datetime.now().strftime("%Y.%m.%d")}"
sort: by_weight
...\n\n'''

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        pass
        output_file.write(extra_content + '\n\n' + HEADER)
        with open(input_file_path, 'r', encoding='utf-8') as input_file:
            with open('build/convert_error.txt', 'w', encoding='utf-8') as error_file:
                for line in input_file:
                    # 按制表符分割每行的汉字和编码
                    parts = line.strip().split('\t')
                    if len(parts) == 2:
                        chinese_char = parts[0]
                        codes = [code.strip() for code in parts[1].split(separator)]

                        # 使用转换编码
                        converted_codes = [process_encoding(code,encoding_method) for code in codes]

                        # 拼接转换后的内容
                        output_line = f"{chinese_char}\t{''.join(converted_codes)}\n"
                        output_fuma = f"{chinese_char}={''.join(converted_codes)}"
                        # 写入到新文件
                        output_file.write(output_line)

                        # 加入辅码
                        fuma.add(output_fuma)

                    else:
                        # 将不符合条件的行输出到 error.txt 文件
                        error_file.write(line)

    sorted_fuma = sorted(fuma)
    with open("build/radical_pinyin_flypy.txt", "w", encoding='utf-8') as f:
        f.write("\n".join(sorted_fuma))

    print(f"转换完成，结果保存在 {output_file_path}")

if __name__ == "__main__":

    # gen_dict('build/dict.yaml','build/gen.yaml', separator = "'")
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) < 3:
        print("Usage: python convert_dict.py input_file output_file [encoding_method] [separator]")
    else:
        # Parse command-line arguments
        input_file_path = sys.argv[1]
        output_file_path = sys.argv[2]
        encoding_method = sys.argv[3] if len(sys.argv) > 3 else 'tofly'
        separator = sys.argv[4] if len(sys.argv) > 4 else ' '

        # Call the function with provided arguments
        gen_dict(input_file_path, output_file_path, encoding_method, separator)