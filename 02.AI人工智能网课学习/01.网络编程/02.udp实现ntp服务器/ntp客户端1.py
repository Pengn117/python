from socket import *
ip_port = ('127.0.0.1', 8000)
buffer_size = 1024


udp_client = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('>>').strip()
    
    udp_client.sendto(msg.encode('utf-8'), ip_port)  #获取日期
    data, addr = udp_client.recvfrom(buffer_size)
    print('bear:ntp服务器的标准时间是：',data.decode('utf-8'))
