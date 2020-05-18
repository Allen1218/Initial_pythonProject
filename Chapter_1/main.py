#
# # import sys
# # sys.path.append('C:\\develop\\python_3_8_2\\Code\\test\\Chapter_1\\hello\\package_test')
# #
# # import package_test.hello as hl
# # hl.print_hello()
#
#
# # 类定义
# class Human(object):
#     pass
#
# # 类属性 : 这个属性和类绑定， 并不是和实例绑定
# class Human(object):
#     taisheng = True # 胎生
#
# # 实例属性 ： 这个name是和实例绑定的
# class Human(object):
#     def __init__(self, name): # 构造函数
#         self.name = name
#
# human_a = Human("Allen")
#
#
# # 类方法
# class Human(object):
#     def __init__(self, name): # 构造函数
#         self.name = name
#     def walk(self):
#         print(self.name + " is walking")
#
# human_a = Human("Allen")
# human_a.walk() # Allen is walking
#
# # 继承
# class Man(Human):
#     def __init__(self, name ,has_wife):
#         super(Man, self).__init__(name)  #  等价与调用父类的构造函数
#         self.__has_wife = has_wife
#
#
#

#

# raise NameError("qq", 1111)
# it = iter("hello")
# print(next(it))

# def myGen():
#     print("生成器被执行")
#     yield 1
#     yield 2
#
# myG = myGen()
# print(next(myG)) # 1
# print(next(myG)) # 2

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
