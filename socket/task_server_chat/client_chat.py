import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12346))

#client_socket.sendall("Ahoj, server!".encode())
while True:
    vstup = []
    if vstup != 0:
        client_socket.sendall(input("Zadej cislo: " ).encode())
        response = client_socket.recv(1024).decode()
        print(f"Odpoveď zo servera: {response}")
    else:
        exit()

