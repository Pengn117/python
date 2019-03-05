import socket

phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#买手机
phone.bind(('127.0.0.1', 8000)) #绑定手机卡
phone.listen(5)#开机

print('客服小mm已经接入...请问有什么可以帮您？')
conn, addr = phone.accept() #等电话

while True:
    msg = conn.recv(1024) #收消息
    print('飞飞：', msg.decode('utf-8'))
    msg_response = input('>>:').strip()
    conn.send(msg_response.encode('utf-8'))

conn.close()
phone.close()
