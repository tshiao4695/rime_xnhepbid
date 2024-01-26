'''
我有一个.txt格式的列表，编码格式为utf-8。列表总共有三列，第一列是汉字，第二列是声母，第三列是韵母。声母和韵母都是有26个英文字母构成，没有其他字符。

对于第二列的所有声母，我希望你进行一个替换处理，他们之间的替换关系如下，左边是需要替换的声母，右边是替换后的字母：

zh	v
ch	i
sh	u

对于第三列的所有韵母，我希望你进行一个替换处理，他们之间的替换关系如下，左边是需要替换的韵母，右边是替换后的字母：
uang	l
iang	l
iong	s
ing	k
eng	g
ang	h
ong	s
van	r
uai	k
uan	r
iao	n
ian	m
ua	x
uo	o
ue	t
ui	v
un	y
ao	c
ai	d
an	j
ei	w
en	f
ia	x
ie	p
iu	q
in	b
ve	t
vn	y
ou	z

请你使用python实现，最终输出一个.txt格式的文本列表，编码仍旧为utf-8，分隔符仍旧为tab。

请使用这种形式来让我确定输入和输出文件的名称：
if __name__ == "__main__":
    input_file = "声母韵母拆分字典.txt"  # 输入文件路径
    output_file = "全拼转双拼编码字典.txt"  # 输出文件路径
    process_file(input_file, output_file)
'''

def replace_sounds(input_str):
    sound_mapping = {'zh': 'v', 'ch': 'i', 'sh': 'u'}
    for old_sound, new_sound in sound_mapping.items():
        input_str = input_str.replace(old_sound, new_sound)
    return input_str

def replace_rhymes(input_str):
    rhyme_mapping = {'uang': 'l', 'iang': 'l', 'iong': 's', 'ing': 'k', 'eng': 'g',
                    'ang': 'h', 'ong': 's', 'van': 'r', 'uai': 'k', 'uan': 'r',
                    'iao': 'n', 'ian': 'm', 'ua': 'x', 'uo': 'o', 'ue': 't',
                    'ui': 'v', 'un': 'y', 'ao': 'c', 'ai': 'd', 'an': 'j',
                    'ei': 'w', 'en': 'f', 'ia': 'x', 'ie': 'p', 'iu': 'q',
                    'in': 'b', 've': 't', 'vn': 'y', 'ou': 'z'}
    for old_rhyme, new_rhyme in rhyme_mapping.items():
        input_str = input_str.replace(old_rhyme, new_rhyme)
    return input_str

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    processed_lines = []
    for line in lines:
        columns = line.strip().split('\t')
        if len(columns) == 3:
            columns[1] = replace_sounds(columns[1])
            columns[2] = replace_rhymes(columns[2])
            merged_column = columns[1] + columns[2]
            processed_lines.append('\t'.join([columns[0], merged_column]))

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(processed_lines))

if __name__ == "__main__":
    input_file = "声母韵母拆分字典.txt"  # 输入文件路径
    output_file = "全拼转双拼编码字典.txt"  # 输出文件路径
    process_file(input_file, output_file)


