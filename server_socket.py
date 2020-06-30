import socket
import threading
HEADER=64
PORT=80
SERVER='158.251.91.68'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="DISCONNECT!"

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTIO]: {ADDR} connected")
    connected = True
    while connected:
        msg_length= conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected=False
            print(f"[{ADDR}] {msg}")
            conn.send("Mensaje recibido".encode(FORMAT))

def start():
    server.listen()
    print("[LISTEN]: Server is listening on address {ADDR}")
    while True:
        conn,addr=server.accept()
        thread= threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS: {threading.activeCount() - 1}")

print("[STARTING]: Server is running....")
start()
