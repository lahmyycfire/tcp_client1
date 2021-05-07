import socket

ip_port = ('127.0.0.1', 8081)
BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect_ex(ip_port)

while True:
    msg = input("请输入:").strip()
    if len(msg) == 0: continue

    s.send(msg.encode('utf-8'))
    feedback = s.recv(BUFSIZE)
    print(feedback.decode('utf-8'))

s.close()
