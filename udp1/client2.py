import socket

BUFSIZE = 1024
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

qq_name_dic = {
    '张无忌': ('127.0.0.1', 8081),
    '周芷若': ('127.0.0.1', 8081),
    '赵敏': ('127.0.0.1', 8081),
    '小昭': ('127.0.0.1', 8081)
}

while True:
    qq_name=input('请选择聊天对象: ').strip()
    while True:
        msg=input('请输入消息,回车发送: ').strip()
        if msg == 'quit': break
        if not msg or not qq_name or qq_name not in qq_name_dic: continue
        udp_client.sendto(msg.encode('utf-8'), qq_name_dic[qq_name])

        back_msg,addr = udp_client.recvfrom(BUFSIZE)
        print('来自[%s:%s]的一条消息:\033[1;44m%s\033[0m' % (addr[0], addr[1], back_msg.decode('utf-8')))
