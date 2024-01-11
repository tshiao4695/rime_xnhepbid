from 2fly import tofly
import os

def process_encoding(codes, method):
    if method == 'tofly':
        return tofly("".join(codes))

def gen_dict(input_file_path, output_file_path=None, encoding_method='tofly', separator=' '):
    if output_file_path is None:
        base_name, ext = os.path.splitext(input_file_path)
        output_file_path = f"{base_name}_gen{ext}"

    # 清空输出文件的内容
    with open(output_file_path, 'w', encoding='utf-8'):
        pass

    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            with open('error.txt', 'w', encoding='utf-8') as error_file:
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

                        # 写入到新文件
                        output_file.write(output_line)

                else:
                        # 将不符合条件的行输出到 error.txt 文件
                        error_file.write(line)

    print(f"转换完成，结果保存在 {output_file_path}")

if __name__ == "__main__":
    gen_dict('dict.yaml','gen.yaml', separator = "'")