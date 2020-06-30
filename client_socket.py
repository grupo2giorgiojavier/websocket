import socket
import getmac
HEADER=64
PORT=22
SERVER='192.168.1.85'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="DISCONNECT!"
MAC_CORRECT='CORRECT MAC ADDRESS'
AUTHORIZED_MAC='08:00:27:89:ad:9f'
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)

def handshake():
    msg=getmac.get_mac_address()
    msg_rcv=send(msg)
    if msg_rcv==MAC_CORRECT:
        return True
    else:
        return False

def send(msg):
    message=msg.encode(FORMAT)
    msg_length=len(message)
    send_length= str(msg_length).encode(FORMAT)
    send_length+=b' '*(HEADER-len(send_length))
    client.send(send_length)
    client.send(message)
    return client.recv(2048).decode(FORMAT)

handshake_confirm=handshake()
if handshake_confirm:
    msg=input("Escriba su mensaje:")
    send(msg)
    