import socket, json
import time, sys
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])

s.connect((host, port))
# s.send(x.strip().encode())
x = input("What do you want to Do? 1. view  2. edit 3. see all updated 4. exit\n")
while( x != 4):
    if (x == 1):
        s.send("read")
        data = s.recv(2048)
        data_arr = json.dumps(data)
        print(data_arr.replace("\\", ""))

    if (x == 2):
        s.send("write")
        data = raw_input("Please enter what you want to update\n")
        s.send(data.encode())

    if (x == 3):
        s.send("update")
        data = s.recv(4098)
        data_arr = json.dumps(data)
        print(data_arr.replace("\\", ""))
    x = input("What do you want to Do? 1. view  2. edit 3. see all updated 4. exit\n")
s.send("4")
s.close()
