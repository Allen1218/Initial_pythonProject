import re

# m=re.findall("abc", 'aaaaabccabcc')
# print(m) #['abc', 'abc']
#
# m=re.findall("\d", 'abc1ab2c')
# print(m) #['1', '2']
#
# ## 连续4个数字
# m=re.findall("\d\d\d\d", "123abc1234abc")
# print(m) #['1234']
#
# ## .代表任意字符， * 无限个字符； r---原始的，没有经过转义
# m=re.findall(r"<div>(.*)</div>", "<div>hello</div>")
# print(m) #['hello']
#
# ## 贪婪匹配：
# m=re.findall(r"<div>(.*)</div>", "<div>hello</div><div>world</div>")
# print(m) #['hello</div><div>world']
#
# ## 非贪婪模式：.代表任意字符， * 无限个字符； r---原始的，没有经过转义
# m=re.findall(r"<div>(.*?)</div>", "<div>hello</div><div>world</div>")
# print(m) #['hello', 'world']
#
# a = "<div>指数</div>"
# word = re.findall('<div>(.*?)</div>', a)
# print(word)

### 2
# 匹配除过换行符之外的所有字符
m=re.findall(".", "aa\nbbcc")
print(m) #['a', 'a', 'b', 'b', 'c', 'c']

# 转义字符
m=re.findall("\.", "a.c")
print(m) #['.']

# 字符集
m=re.findall("a[bcd]e", "abeaceade")
print(m) #['abe', 'ace', 'ade']

# 数字
m=re.findall("\d", "abc1ab2c")
print(m) #['1', '2']

# 非数字
m=re.findall("\D", "abc1ab2c")
print(m) #['1', '2']

# 空白字符 : \s代表正则表达式中的一个空白字符（可能是空格、制表符、其他空白）。
m=re.findall("\s", "abc a\tb2c")
print(m) #['1', '2']

# 非空白字符
m=re.findall("\S", "abc a\tb2c")
print(m) #['1', '2']

# PS:下面看下正则表达式 \w \s \d \b
#
# . 匹配除换行符以外的任意字符
#
# \w 匹配字母或数字或下划线或汉字 等价于 '[^A-Za-z0-9_]'。
#
# \s 匹配任意的空白符
#
# \d 匹配数字
#
## \b 匹配单词的开始或结束
#
# ^ 匹配字符串的开始
#
# $ 匹配字符串的结束
#w
# \w能不能匹配汉字要视你的操作系统和你的应用环境而定
# 非数字和字母 : \w 匹配字母或数字或下划线或汉字 等价于 '[^A-Za-z0-9_]'
m=re.findall("\w", "abc a啊a\tb2c")
print(m) #['a', 'b', 'c', 'a', '啊', 'a', 'b', '2', 'c']

#匹配开头
m=re.findall("^abc", "abcaab2c")
print(m)

#匹配结尾
m=re.findall("abc$", "abcaab2cabc")
print(m)

# 不区分大小写
# re.S (使 . 匹配包括换行在内的所有字符)
# re.I(不区分大小写)
# re.M(多行匹配)
m=re.findall("abc", "abcABC", re.I)
print(m)

# 匹配换行
s = "<div>hello\nworld</div>"
m=re.findall(r"<div>(.*)</div>", s, re.S | re.I)
print(m)

# 匹配一个或0个
m=re.findall("ab？", "abbbbab")
print(m)

# 匹配至少一个 ： 匹配前面的子表达式一次或多次。要匹配 + 字符，请使用 \+。
m=re.findall("ab+", "abbbbab")
print(m)

# 匹配至少0个
m=re.findall("cd*", "cddddeee")
print(m)

#匹配邮箱
m = re.findall("\w+@\w+\.org", "584709796@qq.com;111111@qq.org")
print(m)
for t in m:
    print(t)