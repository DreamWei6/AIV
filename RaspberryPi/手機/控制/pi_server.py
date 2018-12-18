import RBBMove
from socket import *
from time import ctime
import sys

ctrCmd = ['s','a','f','r','l','b']
HOST = ''
PORT = 21567

s = socket(AF_INET, SOCK_STREAM) #創建TCP服務


try:
    s.bind((HOST,PORT))   #绑定地址（host,port）到socket， 在AF_INET下,以元组（host,port）的形式表示地址。
except socket.error as err:
    print("Bind Failed, Error Code: "+ str(err[0])+", Message: "+err[1])
    sys.exit()

print("Socket Bind Success!")

s.listen(10)   #開始TCP監聽,設定最大連接數量,最少為1
print("Socket is now listening")


while True:
        conn, addr = s.accept()
        print('connected from ',addr[0] + ":" + str(addr[1]))
        buf = conn.recv(64) #接收最大bytes
        print(buf)
        text = str(buf)   #text[0] = IP,text[1] = PORT,text[2] = 指令
        if ctrCmd[0] in text[2]:
            RBBMove.stop()
        elif ctrCmd[1] in text[2]:
            RBBMove.auto()
        elif ctrCmd[2] in text[2]:
            RBBMove.forward()
        elif ctrCmd[3] in text[2]:
            RBBMove.right()
        elif ctrCmd[4] in text[2]:
            RBBMove.left()
        elif ctrCmd[5] in text[2]:
            RBBMove.back()

s.close()
