import socket

ip_port = ('127.0.0.1', 8081)
BUFSIZE = 1024

utp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input('请输入日期格式，比如(‘%Y %m %d):').strip()
    utp_client.sendto(msg.encode('utf-8'), ip_port)
    back_msg, addr = utp_client.recvfrom(BUFSIZE)
    print('当前时间：', back_msg.decode('utf-8'))