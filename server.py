import socket
import threading

socketServer = socket.socket()

host = socket.gethostname()
port = 5000

socketServer.bind((host, port))

socketServer.listen(3)

clients=[]

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            clients.remove(client)

def handle(client):
    while True:
        data=client.recv(1024)
        broadcast(data)

def receive():
    while True:
        client, addr = socketServer.accept()

        clients.append(client)

        handleThread=threading.Thread(target=handle, args=(client,))
        handleThread.start()

receive()