# 前言
用搜狗用的很习惯，也一度想学习五笔。但是最后感觉五笔确实没什么逻辑可言。现在隐隐也觉得即使带有逻辑体系的构字法产生，也会相对输入的很麻烦(只是猜测，也许并非如此)
但是搜狗这个产品呀，就是广告太多。要不就是非输入法功能的东西太多。所以就渐渐不想用了。
就东拼西凑搞了个这个奇怪的输入法。

# 使用方法
直接把下载得到的包解压覆盖用户文件夹即可。

1. ac 前缀：小鹤双拼键位查询
3. aw 前缀：单词模式。可进行英文辅助输入。
4. ae 前缀：emoji 模式。可输入英文展示出一些表情。
5. ap 前缀：临时全拼模式。
6. ab 笔画输入模式，相当于搜狗U模式
7. az 拆字输入模式，相当于搜狗U模式
8. tab 辅助码直接扩展在双拼后面，相当于搜狗tab模式
9. 默认小鹤双拼模式，也只有小鹤双拼模式，不支持全拼
10.  用户自定义短语，内含大量数学、逻辑符号、希腊字符
11.  词库扩充，使用了日常语言的高频短语、词组，能够满足日常语句流输入
12.  词库扩充，使用了大量生活词库(饮食、旅游、地理)、生产词库(化工、材料、电子、电力、机械、计算机)、学术词库(数学、物理、化学、心理学)、

# 注意事项
免费公开。只是呼吁有人能做个更加纯粹的输入法。最好也能做个基本构件的输入法，就像英文输入那样，零重码。毕竟输入法这种东西，实在是太基础了。
尽管使用的大多是公开免费使用的依赖，但如果依赖包存在侵权，请联系我进行删除。具体的引用来源如下介绍，一般只贴其他人已经综合好的来源。

我的工作没有啥技术含量，但是为了区分多个输入法的使用方法不同，因此修改了输入法的名称为小鹤拼拆。如果哪里有冒犯或者侵权，请联系我，我会进行修改或者删除。



# 制作方法

## 介紹

【关键字】 RIME / 中州韵 / 小狼毫 / 鼠须管 / 同文 输入法 模仿 类似 搜狗输入法 TAB / U 键 拆字 / 拆部首 / 偏旁 / 构件 / 笔画 的配置文件 / YAML

【背景】由于搜狗输入法过于商业化，导致会产生一些较大的风险，使用去广告版更不可取。因此希望使用一种开源的可控度较高的输入法。而RIME输入法虽然满足风险控制要求，但是对于一般人来说，不容易进行配置。因此需要一个能够把搜狗输入法移植到RIME上的方案。

【过程】

方案1：高度类似搜狗输入法的TAB功能

通过正则表达式对输入码进行重组，使其构成为：双拼码+提示词+辅助码(构件读音的双拼)

步骤如下

https://tieba.baidu.com/p/2094178562

方案2：不完全类似搜狗输入法的TAB功能

类似于U键这样的功能，无法整句输入的同时进行辅助码筛选。

现成方案如下

https://gitee.com/functoreality/rime-flypy-zrmfast

该作者将U模式的提示词'U'改为了'ab'

个人主观感受：自然码的学习成本较高，懒得学习。宁愿把时间花在折腾输入法本身上，也不愿意学自然码这类强行拆解汉字构件的形码 (指不依照说文解字的规则强行拆解构件，使得汉字形码仅保留了文字形状但丧失其原有指称的行为，尽管说文解字也有强行附会的许多字，但更让人无法接受的是当代工程师在文化继承上面的欠考虑，我宁愿重码多一点输入慢一点也不愿意使用没逻辑强行靠记的输入法) 。尤其是可以使用双拼来指向可拆构件的时候，也没有很强烈的需求去专门学习一个不太直观的输入法。

方案3：

        工具清单：ChatGPT、python、excel、互联网搜索引擎
    
        步骤1、获取简繁汉字GBK库所有汉字的合理可拆构件库；
    
        步骤2、将每个构件赋予其造字本义与读音；
    
        步骤3、将每个汉字的构件拆分表替换为构件拆分读音小鹤双拼形式； //以上三个步骤需要文字功底，我直接引用的他人成果，汉字拼音使用[https://github.com/mirtlecn/rime-radical-pinyin]。
    
        步骤4、让GPT编写python表格处理程序，将GBK汉字的读音和构件的双拼按rime-flypy-zrmfast的输入规则整合起来；

//后续考虑把笔画辅助检索也放进这个构件拆分的字典中，因为感觉使用前缀还是比较麻烦。

//由于想要偷懒，所以对于原版小鹤双拼的单韵母部分我采用了双写韵母的方式编码。因为这样偷懒会产生大量的重码，但我不知道怎么解决而且花费的时间较多，所以近期用着没什么问题的话，我也就懒的在折腾这个了。如果后面用的确实重码太高太麻烦了。会想办法把它变换为小鹤双拼原版的编码。之所以麻烦，是因为这个输入法并没有采用RIME的变换处理，而是直接把字典进行小鹤双拼的编码。当然一种可能的解决办法是通过python去进行判断每个韵母前面是否有声母，如果是无声母的，那么就不进行转换即可。

例如：
汉字	拼音	编码
爱	ai	dd(小鹤拼拆)
爱	ai	ai(小鹤双拼)

        步骤5、将rime-flypy-zrmfast的customer文件进行配置，为了拟合搜狗的tab模式，因此修改了无需'['引导的方式。并且将ab前缀功能改成了笔画辅助功能；
           
        步骤6、完成。

用法：

用户自定义短语：

        修改custom_phrase.txt文件可以添加数学符号、语文标点等短语或字符。

前缀模式功能简述：

        ac 前缀：小鹤双拼键位查询；
    
        aw 前缀：单词模式；
    
        ae 前缀：emoji 模式；
    
        ap 前缀：临时全拼模式；
    
        ab 前缀：笔画组字模式；


## 生成步驟說明

第一步、獲取構件字典；
第二步、獲取全拼字典；
第三步、構件字典轉換爲構件拼音字典；
第四步、全拼字典拆分聲母和韻母、替換爲雙拼編碼；
第五步、構件拼音字典拆分聲母和韻母、替換爲雙拼編碼；
第六步、合併雙拼與構件雙拼；
第七步、導入到字典文件中；
第八步、重新部署，完成。

備註：省略了一些細節的步驟，以過於簡單故。

# 第一次更新内容

解決了zh、ch、sh(即zang、cang、sang)的輸入不顯示問題。
解決了小鶴雙拼編碼不符合標準的問題，即ai、an等雙元音韻母的編碼不是an而是jj這類雙寫問題，使得更新後符合標準小鶴編碼。
添加了一些新的自定義短語。

版本：2024.01.26

# 第二次更新内容：

## 完成1 希腊字母大写 - 自定义短语 - 

​	添加了大写字母到schema中speller的alphabet和initials

## 完成2 候选词优先级

​	要改词表

## 完成3 常用汉语词汇/词库导入。添加了搜狗词库 -日常词库、学术词库-

## 完成4 存档与更新说明

## 完成5 许多莫名其妙的同音字需要删除

例如：续约和需要竟然是同音

### 办法：替换词库

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



## 完成6 左右shift 字母上屏

## 完成7 az 引导不带拼音的拆字输入

## 完成8 使用TAB直接引导拆字码


版本: 2024.05.02

