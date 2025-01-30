import socket
import threading

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5555))
server.listen()

clients = []

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            for c in clients:
                c.send(message.encode())
        except:
            clients.remove(client)
            break

while True:
    client, addr = server.accept()
    clients.append(client)
    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
