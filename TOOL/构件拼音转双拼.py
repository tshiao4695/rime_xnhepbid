def split_single_letter_pinyin(single_letter_pinyin):
    if single_letter_pinyin in ["a", "e", "o"]:
        return f"{single_letter_pinyin}\t{single_letter_pinyin}"
    else:
        return single_letter_pinyin

def split_double_vowel(vowel):
    vowels_mapping = {
        "ai": "a\tei",
        "ei": "e\tei",
        "ui": "u\ti",
        "ao": "a\to",
        "ou": "o\tu",
        "iu": "i\tu",
        "ie": "i\te",
        "ue": "u\te",
        "er": "e\tr",
        "an": "a\tn",
        "en": "e\tn",
        "in": "i\tn",
        "un": "u\tn",
        "ang": "a\tang",
        "eng": "e\teng",
    }

    return vowels_mapping.get(vowel, vowel)

def split_zero_initial(zero_initial):
    return f"{zero_initial[0]}\t{zero_initial}"

def split_pinyin(pinyin):
    if len(pinyin) == 1:
        return split_single_letter_pinyin(pinyin)

    zero_initials = ["ang", "eng"]
    initials = ["zh", "ch", "sh", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "r", "z", "c", "s", "y", "w"]
    
    for zero_initial in zero_initials:
        if pinyin.startswith(zero_initial):
            return split_zero_initial(pinyin)

    for initial in initials:
        if pinyin.startswith(initial):
            return f"{initial}\t{pinyin[len(initial):]}"

    # Check for double vowels
    if len(pinyin) == 2 and pinyin in ["ai", "ei", "ui", "ao", "ou", "iu", "ie", "ue", "er", "an", "en", "in", "un", "ang", "eng"]:
        return split_double_vowel(pinyin)

    # If no match found, return the original pinyin
    return pinyin

def replace_initial(initial):
    replacements = {"zh": "v", "ch": "i", "sh": "u"}
    return replacements.get(initial, initial)

def replace_final(final):
    replacements = {
        "uang": "l", "iang": "l", "iong": "s", "ing": "k",
        "eng": "g", "ang": "h", "ong": "s", "van": "r",
        "uai": "k", "uan": "r", "iao": "n", "ian": "m",
        "ua": "x", "uo": "o", "ue": "t", "ui": "v",
        "un": "y", "ao": "c", "ai": "d", "an": "j",
        "ei": "w", "en": "f", "ia": "x", "ie": "p",
        "iu": "q", "in": "b", "ve": "t", "vn": "y",
        "ou": "z"
    }
    return replacements.get(final, final)

def split_zero_initial(zero_initial):
    return f"{zero_initial[0]}\t{replace_final(zero_initial)}"

def split_pinyin(pinyin):
    if len(pinyin) == 1:
        return split_single_letter_pinyin(pinyin)

    zero_initials = ["ang", "eng"]
    initials = ["zh", "ch", "sh", "b", "p", "m", "f", "d", "t", "n", "l", "g", "k", "h", "j", "q", "x", "r", "z", "c", "s", "y", "w"]

    for zero_initial in zero_initials:
        if pinyin.startswith(zero_initial):
            return split_zero_initial(pinyin)

    for initial in initials:
        if pinyin.startswith(initial):
            return f"{replace_initial(initial)}\t{replace_final(pinyin[len(initial):])}"

    # Check for double vowels
    if len(pinyin) == 2 and pinyin in ["ai", "ei", "ui", "ao", "ou", "iu", "ie", "ue", "er", "an", "en", "in", "un", "ang", "eng"]:
        return split_double_vowel(pinyin)

    # If no match found, return the original pinyin
    return pinyin

def process_line(line):
    columns = line.strip().split('\t')
    new_columns = [columns[0]]

    for pinyin in columns[1:]:
        pinyin_list = [split_pinyin(s) for s in pinyin.split('\'')]
        new_columns.extend(pinyin_list)

    return '\t'.join(new_columns)

def process_file(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        for line in infile:
            new_line = process_line(line)
            outfile.write(new_line + '\n')

if __name__ == "__main__":
    input_file = "汉字构件拼音字典.txt"  # 输入文件路径
    output_file = "汉字构件小鹤双拼字典.txt"  # 输出文件路径
    process_file(input_file, output_file)
