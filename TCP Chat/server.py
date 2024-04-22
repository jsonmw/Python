import threading
import socket

host = '127.0.0.1' # localhost, enter server IP here if external
port = 43873       # arbitrary, non well-known port to serve from

# creates a new socket object to represent the server

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host,port))
server.listen()

client_list = []  # holds the socket objects representing a client
nicknames = []    # holds the given nickname of each client

# Sends the given message to all clients with active connections

def broadcast(message):
    for client in client_list:
        client.send(message)

# Will attempt to receive and relay messages received by the given
# client. If this attempt fails, will disconnect the client and
# remove them from the list, notifying other clients.

def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = client_list.index(client)
            nickname = nicknames[index]
            client_list.remove(client)
            client.close()
            broadcast(f'{nickname} left the chat.'.encode('ascii')) # an f-string is format string like printf in C
            nicknames.remove(nickname)
            break

# Receiving new connect using the .accept() function. Prompts the user
# to send their preferred nickname and adds them to the client_list and
# nicknames list. Notifies other users a new client has joined and starts
# a new thread to handle this connection.

def receive():
    while True:
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')

        nicknames.append(nickname)
        client_list.append(client)

        print(f'Nickname of the client is {nickname}!')
        broadcast(f'{nickname} joined the chat.'.encode('ascii'))
        client.send('Connected to the server.'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

print("Server is listening.")
receive()