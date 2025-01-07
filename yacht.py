import socket

HOST = "10.64.18.29"  # Replace with the server's IP address
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    while True:
        data = client.recv(1024).decode()
        if not data:
            break
        print(data, end="")
        if "Enter" in data or "Choose" in data:
            client.send(input().strip().encode())