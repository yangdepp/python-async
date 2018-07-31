import socket

# ipv4(服务端到服务端的通信)类型   对应协议
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
sock, addr = server.accept()

# 获取从客户端发送的数据,每次获取1kb
while True:
    data = sock.recv(1024)
    print(data.decode('utf8'))
    re_data = input()
    sock.send(re_data.encode('utf8'))
    # server.close()
    # sock.close()
