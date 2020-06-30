import socket
import threading
HEADER=64
PORT=3074
SERVER='192.168.1.85'
ADDR=(SERVER,PORT)
FORMAT='utf-8'
DISCONNECT_MESSAGE="DISCONNECT!"
MAC_CORRECT='CORRECT MAC ADDRESS'
AUTHORIZED_MAC='08:00:27:89:ad:9f'
CORRECT_MAC=False
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION]: {ADDR} connected")
    connected = True
    while connected:
        msg_length= conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length=int(msg_length)
            msg=conn.recv(msg_length).decode(FORMAT)
            if msg==AUTHORIZED_MAC:
                print(f"AUTHORIZED MAC [{AUTHORIZED_MAC}] HAS JUST ENTERED THE SERVER")
                conn.send(MAC_CORRECT.encode(FORMAT))
                CORRECT_MAC=True
                while CORRECT_MAC:
                    msg_length=int(msg_length)
                    msg=conn.recv(msg_length).decode(FORMAT)
                    if msg==DISCONNECT_MESSAGE:
                        connected=False
                        CORRECT_MAC=False
                    print(f"[{ADDR}] {msg}")
                    conn.send("Mensaje recibido".encode(FORMAT))

            conn.send("PLEASE SEND YOUR MAC FIRST".encode(FORMAT))

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
