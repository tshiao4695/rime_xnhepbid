# 前言
用搜狗用的很习惯，也一度想学习五笔。但是最后感觉五笔确实没什么逻辑可言。现在隐隐也觉得即使带有逻辑体系的构字法产生，也会相对输入的很麻烦(只是猜测，也许并非如此)
但是搜狗这个产品呀，就是广告太多。要不就是非输入法功能的东西太多。所以就渐渐不想用了。
就东拼西凑搞了个这个奇怪的输入法。

# 使用方法
直接把下载得到的包解压覆盖用户文件夹即可。

1. ab 笔画输入模式，相当于搜狗U模式
2. az 拆字输入模式，相当于搜狗U模式
3. tab 辅助码直接扩展在双拼后面，相当于搜狗tab模式
4. 默认小鹤双拼模式，也只有小鹤双拼模式，不支持全拼
5.  用户自定义短语，内含大量数学、逻辑符号、希腊字符
6.  词库扩充，使用了日常语言的高频短语、词组，能够满足日常语句流输入
7.  词库扩充，使用了大量生活词库(饮食、旅游、地理)、生产词库(化工、材料、电子、电力、机械、计算机)、学术词库(数学、物理、化学、心理学)、

# 注意事项
免费公开。只是呼吁有人能做个更加纯粹的输入法。最好也能做个基本构件的输入法，就像英文输入那样，零重码。毕竟输入法这种东西，实在是太基础了。
尽管使用的大多是公开免费使用的依赖，但如果依赖包存在侵权，请联系我进行删除。具体的引用来源如下介绍，一般只贴其他人已经综合好的来源。

# 第一次更新内容
【介紹】

https://blog.csdn.net/m0_72077882/article/details/135653733?spm=1001.2014.3001.5502

【生成步驟說明】

第一步、獲取構件字典；
第二步、獲取全拼字典；
第三步、構件字典轉換爲構件拼音字典；
第四步、全拼字典拆分聲母和韻母、替換爲雙拼編碼；
第五步、構件拼音字典拆分聲母和韻母、替換爲雙拼編碼；
第六步、合併雙拼與構件雙拼；
第七步、導入到字典文件中；
第八步、重新部署，完成。

備註：省略了一些細節的步驟，以過於簡單故。

【更新說明】

解決了zh、ch、sh(即zang、cang、sang)的輸入不顯示問題。
解決了小鶴雙拼編碼不符合標準的問題，即ai、an等雙元音韻母的編碼不是an而是jj這類雙寫問題，使得更新後符合標準小鶴編碼。
添加了一些新的自定義短語。

版本：202401261002

# 第二次更新内容：

完成1 希腊字母大写 - 自定义短语 - 
	添加了大写字母到schema中speller的alphabet和initials

完成2 候选词优先级
	要改词表

完成3 常用汉语词汇/词库导入。添加了搜狗词库 -日常词库、学术词库-

完成4 存档与更新说明

完成5 许多莫名其妙的同音字需要删除
例如：续约和需要竟然是同音
办法：替换词库

关于小狼毫基本现代汉语常用全拼词库应用于双拼模式下的办法
背景原因：单字的小狼毫输入法简直是毫无人性。然而大多数的拼音输入是语句流。即使是高频词库导入，也解决不了这个问题。甚至还会南辕北辙。因此迫切需要一个汇编了日常语言高频使用的短语库。
如果直接使用全拼词库放进小鹤拼拆，则会出现需要使用全拼的情况，使用双拼无法映射出语句，这是非常要命的。

	第一步、下载清华大学开源词库
https://github.com/iDvel/rime-ice?tab=readme-ov-file
这里直接用汇编好的版本。
	
 	第二步、利用WPS表格将注释行全部删除。
	
 	第三步、将词库复制回notepad++，使用全匹配模式先替换掉
eng	eg
ang	ah

	第四步、使用不完全匹配替换掉
uang	l
iang	l
iong	s
ing	k
eng	g
ang	h
ong	s

ian	m
uan	r
van	r
uai	k
iao	n

iu	q
ue	t
ve	t
un	y
vn	y
uo	o
ie	p
ua	x
ia	x
ui	v
in	b
ei	w
ai	d
en	f
an	j
ou	z
ao	c

zh	v
ch	i
sh	u

	第五步、使用完全匹配替换掉
a	aa
o	oo
e	ee
d	ai
f	en
j	an
z	ou
c	ao

	第六步、导入词库，完成。

完成6 左右shift 字母上屏

完成7 az 引导不带拼音的拆字输入

完成8 使用TAB直接引导拆字码


version: 2024.05.02

