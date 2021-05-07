import socket
from time import strftime

ip_port = ('127.0.0.1', 8081)
BUFSIZE = 1024
utp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
utp_server.bind(ip_port)

while True:
    msg, addr = utp_server.recvfrom(BUFSIZE)
    print('===>', msg)

    if not msg:
        time_fmt = '%Y-%m-%d %X'
    else:
        time_fmt = msg.decode('utf-8')

    back_msg = strftime(time_fmt)

    utp_server.sendto(back_msg.encode('utf-8'), addr)