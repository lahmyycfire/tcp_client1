import socket

ip_port = ('127.0.0.1', 8081)
BUFSIZE: int = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(ip_port)
s.listen(5)

while True:
    conn, addr = s.accept()
    print('conn:%s' % conn)
    # print('addr:%s' % addr)
    print('接到来自[%s]的电话' % addr[0])
    while True:
        msg = conn.recv(BUFSIZE)
        if len(msg) == 0:
            break

        print(msg, type(msg))
        conn.send(msg.upper())

    conn.close()

# s.close()