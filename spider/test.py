# # tcp server
# import socket
#
# host = '127.0.0.1'  # Local Server IP
# host2 = '152.135.85.246'  # Real Server IP
# port = 8080  # Local Server Port
# port2 = 8080  # Real Server Port
#
#
# def ProcData(data):
#     return data
#     # add more code....
#
#
# print("Map Server start from " + host + ":" + str(port) + " to " + host2 + ":" + str(port2) + "\r\n")
#
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(('127.0.0.1', port))
# print("127.0.0.1 Server start at " + str(port) + "\r\n")
#
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect((host2, port2))
# print(host + " Client connect to " + host2 + ":" + str(port2) + "\n")
#
# server.listen(5)
# ss, addr = server.accept()
# print('got connected from', addr)
#
# while 1:
#     msg = ss.recv(204800000)
#     print  ("Get:" + repr(msg) + "\r\n")
#
#     client.send(msg)
#     print ("Client send data %s to "%repr(msg))
#     buf = client.recv(204800000)
#
#     print("Client recv data %s from "%repr(buf))
#     ss.send(buf)
#     print("Send:" + repr(buf) + "\r\n")

#pyinstaller -F test.py
#pyinstaller -F -i  cat_500600.jpg

print("提示：1.源文件请命名为 source.log !")
print("提示：2.输出的文件名为 OutPut.txt!")

str = input("请输入，您要保留行的关键字：")
print ("您输入的保留行关键字是(例如 DTPFsrv.1): ", str)

b=[x for x in open('DLC017700GBPH31A7_UOP.log').readlines() if x.find(str)>-1]
with open('OutPut_DLC017700GBPH31A7_UOP.txt','w') as f:
    f.writelines(b)