import socket

from server import DISCONNECT_MESSAGE, FORMAT

HEADER = 64
FORMAT = 'utf-8'
SERVER = '192.168.1.10'
PORT = 5050
ADDR = (SERVER, PORT)
DISCONNECT_MESSAGE = 'DISCONNECT!'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length =  len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - send_length)
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send("Hello World!")
send(DISCONNECT_MESSAGE)


