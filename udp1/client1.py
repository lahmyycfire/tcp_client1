import socket

BUFSIZE = 1024
udp_server_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

qqname_dic = {
    '张无忌': ('127.0.0.1', 8081),
    '周芷若': ('127.0.0.1', 8081),
    '赵敏': ('127.0.0.1', 8081),
    '小昭': ('127.0.0.1', 8081)
}

while True:
    qqname = input('请输入要聊天的人：').strip()
    while True:
        msg = input("请输入聊天内容:").strip()
        if msg == 'quit': break
        if not msg or not qqname or qqname not in qqname_dic: continue
        udp_server_client.sendto(msg.encode('utf-8'), qqname_dic[qqname])

        back_msg, addr = udp_server_client.recvfrom(BUFSIZE)
        print('来自[%s:%s]的一条消息:\033[1;44m%s\033[0m' %(addr[0],addr[1],back_msg.decode('utf-8')))