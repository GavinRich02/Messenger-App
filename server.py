#imports
import socket
import threading


#initializes server
socket = socket.socket()

host = socket.gethostname()
port = 5000

socket.bind((host, port))

#Adjustable; Total number of connections that the program allows
socket.listen(3)

#array for client IP's
clients=[]

#sends message to all clients
def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:
            clients.remove(client)

#checks for/receives data from clients
def handle(client):
    while True:
        data=client.recv(1024)
        broadcast(data)

#allows client access and initializes handle thread
def receive():
    while True:
        client, addr = socket.accept()

        clients.append(client)

        handleThread=threading.Thread(target=handle, args=(client,))
        handleThread.start()

receive()