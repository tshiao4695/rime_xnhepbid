import sys

# 读取文本文件，解析每一行，构建字典
def parse_text_files(file_path1, file_path2):
    set_a = {}  # 集合A的字典，用于存储字符和相应内容的关系
    set_b = {}  # 集合B的字典，用于存储内容和相应字符的关系

    # 读取第一个文件
    with open(file_path1, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            columns = line.strip().split('\t')
            char = columns[0]  # 第一列字符
            content = columns[1] if len(columns) > 1 else ''  # 第二列内容，确保有足够的列

            # 更新集合A的字典
            if char in set_a:
                set_a[char].append(content)
            else:
                set_a[char] = [content]

    # 读取第二个文件
    with open(file_path2, 'r', encoding='utf-16LE', errors='ignore') as file:
        for line in file:
            columns = line.strip().split('\t')
            char = columns[0]  # 第一列字符
            content = columns[1] if len(columns) > 1 else ''  # 第二列内容，确保有足够的列

            # 更新集合B的字典
            if char in set_b:
                set_b[char].append(content)
            else:
                set_b[char] = [content]

    return set_a, set_b

# 生成集合C
def generate_set_c(set_a, set_b):
    set_c = {}  # 集合C的字典，用于存储字符和内容组合的结果

    # 遍历集合A和集合B中相同的字符，分别组成两个数组
    for char in set_a.keys() & set_b.keys():
        array_a = set_a[char]
        array_b = set_b[char]

        # 对两个数组进行两两组合
        combined_values = [a + '[' + b for a in array_a for b in array_b]

        # 更新集合C的字典
        set_c[char] = combined_values

    return set_c

# 保存结果到文件
def save_set_c_to_file(set_c, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        for char, values in set_c.items():
            for value in values:
                # 将每个值写入新的行，第一列保留原来的字符
                file.write(f'{char}\t{value}\n')

if __name__ == "__main__":
    # 填写文件路径和名称
    file_path1 = '全拼转双拼编码字典.txt'
    file_path2 = '构件双拼合并.txt'
    result_file_path = '最终拼拆字典文件.txt'

    # 解析文本文件，生成集合C，并保存结果
    set_a, set_b = parse_text_files(file_path1, file_path2)
    set_c = generate_set_c(set_a, set_b)
    save_set_c_to_file(set_c, result_file_path)
