import socket
from _thread import *
import sys
import time
from Game_status import *

Apos = 0
Bpos = 0
client_names = []
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


# If someone win, he should send a FIN.
# The reponse message should be END if the game already has a winner,
# or RUN if still running.
def player_thread(name, conn):
    global game_status
    current_pos = 0
    while True:
        data = conn.recv(2048).decode("utf-8")
        if (data == "FIN"):
            game_status = Game_status.SOMEONE_WIN
        elif (name != "display"):
            data = data.split(',')
            nowpos = int(data[0])
            speed = float(data[1])
            # TODO Here Should send to TBDisplayServer for display.
            if (name == client_names[0]):
                Apos = nowpos
            elif (name == client_names[1]):
                Bpos = nowpos
            print("{}:  {}".format(name, (nowpos, speed)))
            if game_status == Game_status.SOMEONE_WIN:
                conn.send(str.encode("END"))
            else:
                conn.send(str.encode("RUN"))
        else:
            conn.send(str.encode("{}, {}".format(Apos, Bpos)))
        


def client_thread(conn):
    try:
        client_name = conn.recv(2048).decode("utf-8")
        print("Client named \"{}\" comes in.".format(client_name))
        if (client_name == "display"):
            display_online = True
        else :
            client_names.append(client_name)
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
