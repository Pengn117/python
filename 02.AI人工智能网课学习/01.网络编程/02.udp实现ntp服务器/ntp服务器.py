from socket import *
import time

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

ntp_server = socket(AF_INET, SOCK_DGRAM)
ntp_server.bind(ip_port)

while True:
    data, addr = ntp_server.recvfrom(buffer_size)
    print('当前连接的主机是：',addr)
    if not data:
        fmt = '%Y-%m-%d %X'
    else:
        fmt = data.decode('utf-8')

    back_time = time.strftime(fmt)
    ntp_server.sendto(back_time.encode('utf-8'),addr)
    
