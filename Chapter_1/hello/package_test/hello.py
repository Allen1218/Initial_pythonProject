# """print("hello world")
#
# print("hello world")
#
# print("hello world")"""
# #
# # # username = input('请输入用户名')
# # # print(username)
# # ###########################
# # print("hello world")
# #
# # ##  print(*objects, sep='', end='\n', file=sys.stdout, flush=False)
# #
# # print('2020', '02', '29', sep='-')
# #
# # #file
# # file_source = open('zen.txt', 'a+', encoding='utf-8')
# # print('人生苦短，我用python', file=file_source)
# # file_source.close()
#
# ### operator
# # **	幂 - 返回x的y次幂
# # //	取整除 - 返回商的整数部分（向下取整）
#
# # a, b = 5, 10
# # a, b = b, a
# # print(a, b)
#
# # a = 1
# # if a == 1:
# #     print("hello world1")
# #     print("hello world2")
# # else:
# #     print("hello world2")
# # x = -1
# # # y = x if x >= 0 else -x
# # # print(y)
#
# # str = "hello world"
# # for item in str:
# #     if item == "l":
# #         continue
# #     print(item)
# # else:
# #     print("打印完成")
#
# # motto = "abcd,efg"
# # print(motto[0:2])
# # print(motto[1:])
# # print(motto[0:1100:2])
#
#
# str = "the length of (%s) is %d" %('runoob',len('runoob'))
# print(str)
#
# #你好Allen，这是你登录的第3次, 本次消费99.5员
# # name = "Allen"
# # logInTime = 3
# # count = 99.47
# # str = '你好{0}，这是你登录的第{1}次, 本次消费{2:.1f}员'.format('Allen', 3, 99.47)
# # str1 = '你好{name}，这是你登录的第{time}次, 本次消费{count:.1f}元'.format(name=name, time=logInTime, count=count)
# #
# # print(str1)
# #
# # str2 = F'你好{name}，这是你登录的第{logInTime}次, 本次消费{count:.1f}元'
# # print(str2)
# #
# # print(2*"hello ")
#
# # s = 3.1415926
# # num = f'{s:<13}'
# # print(num)
# # type(num)
# # print(f'{123:#0x}')
# # a=123.456
# # print(f'{a:08.2f}') #'00123.46'
# #
# # s="hello"
# # print(f'{s:8.3s}')  #'hel     '
# #
# # b=1234567890.1234567
# # print(f'{b:_g}')
# #
# # list_a = ['aa', 'bb', 'cc']
# # list_a.insert(2, 'ff')
# # print(list_a[0])   # ['aa', 'bb', 'ff', 'cc']
#
# # dict_b ={'s':"Allen", 2:"bob", 3:"lucy"}
# # dict_b.add()
# # print(dict_b['s'])       #Allen
# # print(2 in dict_b)       #True
# # print(dict_b.get('s'))   #Allen
# # print(dict_b.items())    #dict_items([('s', 'Allen'), (2, 'bob'), (3, 'lucy')])
#
#
#
# # tuple_b = ('aa', 'bb', 'cc')
# # print(tuple_b[1])
#
#
# # aList = [ 'Google', 'Runoob', 'Taobao', 'Facebook'];
# #
# # aList.sort();
# # print(aList)
#
#
# # def printme( str="hello" ):
# #    "打印传入的字符串到标准显示设备上"
# #    print (str)
# #    return
# #
# # printme()  # hello
#
# #不定长参数
# # def print_args(s, *args):
# #     print(s,end='  ')
# #     for a in args:
# #         print(a, end='  ')
# #     return
# #
# # # print_args('hello')
# # print_args('aaaa', 'a', 1 ,'b')  # aaaa  a  1  b
#
# # # 参数次序可以变
# # def print_two(a, b):
# #     print(a,b)
# #
# # print_two(b='bb', a='aa')   # aa bb
#
# # def mother():
# #     var = 110
# #     print('mother中的var的值为',var)
# #     def son():
# #         nonlocal var
# #         var = 119
# #         print('Son中的var的值为',var)
# #     print('函数中的var的值为',var)
# #     return son
# #
# # i = mother()
# # i()
#
#
#
#


def print_hello():
    print("hello")
    return
