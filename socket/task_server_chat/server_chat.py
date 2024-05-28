import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12346))
server_socket.listen()

print("Server čaká na pripojenia...")
client_socket, client_address = server_socket.accept()
print(f"Pripojil sa klient: {client_address}")

while True:
    message = client_socket.recv(1024).decode()
    if message == "ahoj":
        print(f"Správa od klienta: {message}")
        client_socket.sendall("Ahoj, toto je odpověň na ahoj ".encode())
    elif message == "ne":
        print(f"Správa od klienta: {message}")
        client_socket.sendall("Správa prijatá 2 ".encode())
    else:
        client_socket.close()
        server_socket.close()