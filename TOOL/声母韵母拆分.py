
'''
生成本篇代码，成功的提示语：
我有一个列表，它是.txt文本格式，它有两列，以tab为分隔符。第一列全部都是一个字的汉字，第二列全部是26个英文字母所组成的拼音，没有声调。我希望能够将第二列的拼音进行分列操作，将拼音的声母和韵母分为两列，并输出一个新的.txt列表文件，第一列是汉字，第二列是声母，第三列是韵母。声母的清单如下：“b、p、m、f、d、t、n、l、g、k、h、j、q、x、r、z、c、s、y、w、zh、ch、sh”，zh、ch、sh这三个声母要比z、c、s这三个声母先进行处理。否则python会把zh拆分成z,h。对于所有只有一个字母的拼音，例如“a、o、e”，你需要转换成“a,a、o,o、e,e”，即双写后再分列。不仅如此，由于许多汉字的拼音并没有声母，即所谓零声母，因此会有许多以“a、e、o”开头的拼音，例如ai、ao、ei、en、ou，我希望这样由两个字母所构成的拼音也进行拆分，这样的拼音有“ei、ai、en、an、ou、ao”这六个，我希望他们会拆分成“e,i、a,i、e,n、a,n、o,u、a,o”。另外还有一些零声母的拼音，他们的拼音是“ang、eng”这两个，我希望他们双写首字母，然后再将第一个字母和后面的字母分列，例如他们会拆分成“a,ang、e,eng”。文本文件的编码是utf-8，输出文件的所有分隔符最终仍旧是tab。请你忽略输入文件第二列之后的列进行处理，为了避免在某些行上没有足够的列数，导致索引错误，需要在访问列表之前确保列表中有足够的元素。请你使用python为我实现这样的功能。
请使用这种形式来让我确定输入和输出文件的名称：if __name__ == "__main__":
    input_file = "全拼编码.txt"  # 输入文件路径
    output_file = "声母韵母拆分字典.txt"  # 输出文件路径
    process_file(input_file, output_file)

'''

'''
本来想用的第二版提示语：

我有一个列表，它是.txt文本格式，它有两列，以tab为分隔符。第一列全部都是一个字的汉字，第二列全部是26个英文字母所组成的拼音，没有声调。

我希望能够将第二列的拼音进行分列操作，将拼音的声母和韵母分为两列，并输出一个新的.txt列表文件，第一列是汉字，第二列是声母，第三列是韵母。

声母的清单如下：“b、p、m、f、d、t、n、l、g、k、h、j、q、x、r、z、c、s、y、w、zh、ch、sh”，zh、ch、sh这三个声母要比z、c、s这三个声母先进行处理。否则python会把zh拆分成z,h。

对于所有只有一个字母的拼音，例如“a、o、e”，你需要转换成“a,a、o,o、e,e”，即双写后再分列。

对于拼音只有两个字母构成的情况，如“ei、ai、en、an、ou、ao”这六个拼音，我希望他们会拆分成“e,i、a,i、e,n、a,n、o,u、a,o”。

对于拼音只有三个字母构成的情况，如“ang、eng”这两个，我希望他们双写首字母，然后再将第一个字母和后面的字母分列，例如他们会拆分成“a,ang、e,eng”。

文本文件的编码是utf-8，输出文件的所有分隔符最终仍旧是tab，而非,这个符号。

请你使用python为我实现这样的功能。

你需要忽略输入文件第二列之后的列进行处理。

为了避免在某些行上没有足够的列数，导致索引错误，需要在访问列表之前确保列表中有足够的元素。

同时，请你使用下面这种形式来让我确定输入和输出文件的名称

if __name__ == "__main__":
    input_file = "全拼编码.txt"  # 输入文件路径
    output_file = "声母韵母拆分字典.txt"  # 输出文件路径
    process_file(input_file, output_file)

'''

def split_pinyin(pinyin):
    result = []
    vowels = "aeiouv"
    zero_initial = {"ang": "a,ang", "eng": "e,eng"}
    single_vowel_mapping = {vowel: f"{vowel},{vowel}" for vowel in vowels}
    double_vowel_mapping = {"ai": "a,i", "ei": "e,i", "ui": "u,i", "ao": "a,o", "ou": "o,u", "iu": "i,u", "ie": "i,e", "ue": "u,e", "ve": "v,e"}

    if pinyin in zero_initial:
        return zero_initial[pinyin].split(',')
    elif len(pinyin) == 1:
        return single_vowel_mapping[pinyin].split(',')
    elif len(pinyin) == 2 and pinyin in double_vowel_mapping:
        return double_vowel_mapping[pinyin].split(',')
    elif len(pinyin) > 2 and pinyin[:2] in double_vowel_mapping:
        return double_vowel_mapping[pinyin[:2]].split(',') + [pinyin[2:]]
    else:
        return [pinyin[0], pinyin[1:]]

def process_file(input_file, output_file):
    initials = ["b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "r", "zh", "ch", "sh", "z", "c", "s", "y", "w"]
    input_lines = []

    with open(input_file, 'r', encoding='utf-8') as file:
        input_lines = file.readlines()

    output_lines = []

    for line in input_lines:
        line = line.strip()
        columns = line.split('\t')

        if len(columns) >= 2:
            char, pinyin = columns[0], columns[1]

            if pinyin:
                initials_mapping = {"zh": "zh", "ch": "ch", "sh": "sh"}

                if pinyin[:2] in initials_mapping:
                    initial = initials_mapping[pinyin[:2]]
                    rest = pinyin[2:]
                elif pinyin[:1] in initials:
                    initial = pinyin[:1]
                    rest = pinyin[1:]
                else:
                    initial, rest = split_pinyin(pinyin)

                output_lines.append(f"{char}\t{initial}\t{rest}")
            else:
                output_lines.append(f"{char}\t\t")
        else:
            output_lines.append(line)

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(output_lines))

if __name__ == "__main__":
    input_file = "全拼编码.txt"  # 输入文件路径
    output_file = "声母韵母拆分字典.txt"  # 输出文件路径
    process_file(input_file, output_file)
