import socket
from _thread import *
import sys
import time
from Game_status import *

client_names = set()
display_online = False
game_status = Game_status.RUNNING

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "localhost"
server_ip = socket.gethostbyname(server)
port = 5295

try:
    s.bind((server, port))
except socket.error as e:
    print(e)

s.listen(3)
print("Server has been established, waiting for connections.")

def check_all_online():
    global client_names, display_online
    # return (len(client_names) == 2 and display_online)
    return len(client_names) == 2

def player_thread(name, conn):
    global game_status
    current_pos = 0
    while True:
        data = conn.recv(2048).decode("utf-8")
        if (data == "FIN"):
            game_status = Game_status.SOMEONE_WIN
        else:
            data = data.split(',')
            nowpos = int(data[0])
            speed = float(data[1])
            print("{}:  {}".format(name, (nowpos, speed)))
        if game_status == Game_status.SOMEONE_WIN:
            conn.send(str.encode("END"))
        else:
            conn.send(str.encode("RUN"))

def client_thread(conn):
    try:
        client_name = conn.recv(2048).decode("utf-8")
        print("Client named \"{}\" comes in.".format(client_name))
        if (client_name == "display"):
            display_online = True
        else :
            client_names.add(client_name)
        while not check_all_online():
            time.sleep(0.1)
        time.sleep(1)

        print("{}: Game begin.".format(client_name))
        while True:
            conn.send(str.encode("BEGIN"))
            try:
                conn.settimeout(0.6)
                result =  conn.recv(2048).decode("utf-8")
                if (result == "RECV"):
                    break
            except socket.timeout:
                continue
        conn.settimeout(None)    

        while True:
            player_thread(client_name, conn)
            
    except Exception as e:
        print(e)
        


while True:
    conn, addr = s.accept()
    print("New connection established from {}.".format(addr))
    start_new_thread(client_thread, (conn,))
