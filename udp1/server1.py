import socket

ip_port = ('127.0.0.1', 8081)
BUFSIZE: int = 1024
udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server_client.bind(ip_port)

while True:
    msg, addr = udp_server_client.recvfrom(BUFSIZE)
    print('收到[%s,%s]的一条消息:\033[1;44m%s\033[0m' % (addr[0], addr[1], msg.decode('utf-8')))
    back_msg = input("回复消息：").strip()
    udp_server_client.sendto(back_msg.encode('utf-8'), addr)