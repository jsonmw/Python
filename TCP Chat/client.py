import socket
import threading

nickname = input("Choose a nickname: ") # accept user input for nickname
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 43873)) # kinda dumb to hardcode this but here we are. can import sys to accept CLI arguments for this

# receives ASCII encoded messages using the socket module .recv() method and decodes them, prints to console. If this connection
# fails, the connection closes.

def receive():
    while True:
	  
	  # python uses try/except instead of try/catch, but they are essentially the same

        try:
		# responds to the server prompt for nickname, only used once
            message = client.recv(1024).decode('ascii')
            if message == 'NICK': # 
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occurred.")
            client.close()
            break

# uses a format string to output

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('ascii'))

# uses a separate thread to handle receiving and writing messages so they can happen concurrently

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()