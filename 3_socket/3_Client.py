import socket

# クライアント側
HOST = '127.0.0.1'
PORT = 55522

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        message = input("Send: ")
        if message == "":
            s.sendall("none".encode())
        else:
            s.sendall(message.encode())
        data = s.recv(1024)
        print(f"Received: {data.decode()}")