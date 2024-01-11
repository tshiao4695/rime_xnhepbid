## 概述

用拼音输入一个汉字的每一个组成部分（偏旁、部首等部件），组合拼出字来。

例如：

1. 输入 `kou kou ma`（口 口 马）或者 `wang ma`（罒 馬）得 `骂（罵）`
2. 输入 `wu niao`（敄 鸟）或者 `mao wen niao`（矛 夂 鸟）得 `鹜`

![image](res/home.png)

适配双拼（上图为小鹤双拼）

## 安装

下载以下两个文件

- radical_pinyin.dict.yaml
- radical_pinyin.schema.yaml

复制到 Rime 用户目录

双拼用户请手动修改 algebra 的 __include 部分

## 反查

在目标输入方案的如下部分写入信息：

```yaml
# apply to example.schema.yaml
schema:
    dependencies:
        - radical_pinyin
    segmentors:
        - affix_segmentor@radical_lookup
    translators:
        - table_translator@radical_lookup
    filters:
        - reverse_lookup_filter@radical_reverse_lookup
    radical_reverse_lookup:
        tags: [ radical_lookup ]
        overwrite_comment: true 
        dictionary: example # 提示码词表
        comment_format:
            - xform/^/(/
            - xform/$/)/
    radical_lookup:
        tag: radical_lookup
        dictionary: radical_pinyin
        prefix: 'u'
        tips: "[拆字]"
        # closing_tips:
        suffix: "'"
        comment_format:
            - erase/^.*$//
    recognizer:
        patterns:
            radical_lookup: "u[a-z]+'?$"
```

按 `u` 引导拆字，效果：

![image](res/home2.png)

## 码表

码表：[chazi](https://github.com/kfcd/chaizi) 

添补 [henrysting](https://github.com/henrysting/chaizi/)

注音、校对、添补：[Mirtle](https://github.com/mirtlecn)

该码表采用 [CC BY 3.0 DEED](https://creativecommons.org/licenses/by/3.0/) 授权条款

更改：

- 合并了繁简两份码表，合入了 henrysting 的添补
- 和常用字比对，加入了 200 多未收录的常用字
- 更正了大量拆法
- 删除了不能正常显示的汉字
- 手动添补了一些原来没有的拆字
- 加入一些其他拆法和汉字（如二叠字）

## 输入方案

by Mirtle

许可证 [LGPL](LICENSE.txt)

## 问题

请提交 issue
