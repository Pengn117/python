import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#买手机
phone.bind(('127.0.0.1', 8000)) #绑定手机卡
phone.listen(5)#开机

print('正在等待客户端发来消息*********')
conn, addr = phone.accept() #等电话

msg = conn.recv(1024) #收消息
print('客户端发来的消息是:', msg)
conn.send(msg.upper())

conn.close()
phone.close()
