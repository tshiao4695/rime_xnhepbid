from datetime import datetime
from itertools import product
import pypinyin
from pypinyin_dict.pinyin_data import kmandarin_8105
import re

HEADER = f'''---
name: radical_pinyin
version: "{datetime.now().strftime("%Y.%m.%d")}"
sort: by_weight
use_preset_vocabulary: true
max_phrase_length: 1
...\n\n'''

pattern = re.compile("^[a-z']+$")
is_not_empty = lambda x: x != ' '
kmandarin_8105.load()

with open("build/error_line.yaml", "w", encoding='utf-8') as error_file_1:
    pass  # Do nothing, just clear the file

with open("build/error_char.yaml", "w", encoding='utf-8') as error_file_2:
    pass 

with open("build/error.yaml", "w", encoding='utf-8') as error_file_3:
    pass

def is_chinese_char_regex(char):
    """Checks if a character is likely a Chinese character using a regular expression."""
    return bool(re.match(r"[\u4e00-\u9fff]", char))

from pypinyin import pinyin, Style, load_phrases_dict
custom_dict = {
    '廾': [['gong4','nong4']],
    '一': [['heng2','yi1']],
    '灬': [['huo3']],
    '丿': [['pie3']],
    '丨': [['shu4']],
    '乁': [['na4']],
    '㇏': [['na4']],
    '⺄': [['yi3']], # 「乙」的变体
    '𠃊': [['zhe2']],
    '𠙽': [['kuai4']],
    '𦉼': [['la4']],
    '𭕘': [['mei2']],
    '𣥚': [['zou3']],
    '𤽄': [['quan2']],
    '疋': [['ding4','pi3','shu1','ya2']],
    '乚': [['gou1']],
    '亅': [['gou1']],
    '𠄌': [['gou1']],
    '凵': [['kan3']],
    '冖': [['mi4','bao3']],
    '攵': [['wen2']],
    '𠃌': [['zhe2','gou1']],
    '夂': [['wen2']],
    '冂': [['tong2','jiong1']],
    '丶': [['dian3']],
    '乛': [['zhe2']],
    '㇆': [['zhe2']],
    '𡗗': [['chun1']],
    '乀': [['na4']],
    '𠃋': [['zhe2']],
    '龴': [['yu3', 'si1']],
    '㇉': [['zhe2']],
    '⺆': [['ji3']],
    '□': [['ge1']],
    '': [['yi1']], # 「衣」去掉 亠 的下部，以及再去掉丿的变体（「展」的下部）
    '卩': [['er3']],
    '廴': [['jian4']],
    '宀': [['bao3']],
    '龷': [['gong4']],
    '□': [['zhe2']],
    '𡕩': [['man3']],
    '罒': [['si4','wang3']],
    '癶': [['deng1']],
    '𠃍': [['zhe2']],
    '爫': [['zhua3','zhao3']],
    '彳': [['ren2','chi4']],
    '阝': [['er3']],
    '匚': [['fang1','kuang1']],
    '彐': [['shan1']],
    '刂': [['dao1']],
    '丬': [['jiang1','qiang2']],
    '囗': [['kou3','wei2','guo2']],
    '辶': [['zou3','zhi1']],
    '彡': [['shan1','san1']],
    '𦣞': [['yi2']]
    # '日': [['ri4','yue1']]
    }
load_phrases_dict(custom_dict)

radical = []
yaml = set()
error_yaml_set = set()

with open("radical.txt", 'r', encoding='utf-8' ) as f:
    radical = f.readlines()

for line in radical:
    line = line.strip()
    if line.startswith("#") or "\t" not in line:
        with open("build/error_line.yaml", "a", encoding='utf-8') as error_file_1:
            error_file_1.write(line + '\n')
        continue

    char, units = line.split("\t", 1)
    if (
        char == "□"
        or len(char) != 1               # Ensures char is only one character
        # or not is_chinese_char_regex(char)    # Checks if char is a valid Chinese character
        # or char in units               # Checks if units contains the character
        # or len(units) == 1
        or not units
        ):
        with open("build/error_char.yaml", "a", encoding='utf-8') as error_file_2:
            error_file_2.write(line + '\n')
        continue

    # unit 是单个拆法不同的拆字部件
    for unit in units.split('\t'):
        # 判断有没有写错的
        # if ( len(unit) == 1 ):
        #     with open("error_char.yaml", "a", encoding='utf-8') as error_file_2:
        #         error_file_2.write(line + '\n')
        #     continue
        # pypinyin 获取拼音
        pinyin_list = pypinyin.pinyin(unit.split(), style=pypinyin.Style.NORMAL, heteronym=True)
        for pinyin in product(*pinyin_list):
            pinyin = "'".join(filter(is_not_empty, pinyin))
            if not pattern.match(pinyin): 
                error_item = f"{char.strip()}\t{pinyin}"
                error_yaml_set.add(error_item)
                continue
            item = f"{char.strip()}\t{pinyin}"
            yaml.add(item)
with open("info.yaml", 'r', encoding='utf-8') as f:
    extra_content = f.read()

sorted_yaml = sorted(yaml)
sorted_error_yaml = sorted(error_yaml_set)

with open("build/error.yaml", "w", encoding='utf-8') as error_file_3:
    error_file_3.write("\n".join(sorted(error_yaml_set)))
with open("build/radical_pinyin.dict.yaml","w",encoding='utf-8') as f:
    f.write(extra_content + '\n\n'  + HEADER + "\n".join(sorted_yaml) + '\n\n')
