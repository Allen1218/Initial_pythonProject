import os
path = r"C:\AMAT\AA"
replaceStr = {'<iostream.h>':'<iostream>', '<aaa.h>': '<aaa>'}

def getFlist():
    L = []
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            #print(name)
            flag = name.endswith(".cpp") or name.endswith(".h")
            if not flag :
                continue

            L.append(os.path.join(root, name))
    return L

# 传入文件(file),将旧内容(old_content)替换为新内容(new_content)
def replace(file):
    content = read_file(file)
    for key in replaceStr:
        print(key)
        old_content = key
        new_content = replaceStr[key]
        content = content.replace(old_content, new_content)

    rewrite_file(file, content)

# 读文件内容
def read_file(file):
    with open(file, encoding='UTF-8') as f:
        read_all = f.read()
        f.close()

    return read_all

# 写内容到文件
def rewrite_file(file, data):
    with open(file, 'w', encoding='UTF-8') as f:
        f.write(data)
        f.close()

# 替换操作(将test.txt文件中的'Hello World!'替换为'Hello Qt!')


def modifyFile(srcflist):
    print('----')

    # 修改.h 文件
    for i in srcflist:
        if i.endswith(".h") :
            print('modify .h filename :' + i)
            replace(i)
def modifyInsertArgs(srcflist):
    for i in srcflist:
        if i.endswith(".h"):
            with open(i, "r", encoding="utf-8") as f:
                lines = f.readlines()

            with open(i, "w", encoding="utf-8") as f_w:
                for line in lines:
                    if not '.insertArgs("%s' in line:
                        continue
                    line = line.replace(line, "ID_NUM = 22")

                    # strlist = line.split(',')  # 用逗号分割str字符串，并保存到列表
                    # for value in strlist:

                    f_w.write(line)

def processFile(srcflist) :
    for i in srcflist:
        # if i.endswith(".h"):
            with open(i, "r", encoding="utf-8") as f:
                lines = f.readlines()

            with open(i, "w", encoding="utf-8") as f_w:
                for line in lines:
                    # if not '.insertArgs("%s' in line:
                    #     continue
                    # if line is ema
                    line=line.strip('\n')
                    a= '<' + line + '>' + '</' + line + '>'+'\n'
                    line = line.replace(line, '<' + line + '>' + '</' + line + '>'+'\n')

                    # strlist = line.split(',')  # 用逗号分割str字符串，并保存到列表
                    # for value in strlist:

                    f_w.write(line)

if __name__ == "__main__" :
    srcflist = getFlist()
    print(srcflist)
    processFile(srcflist)

