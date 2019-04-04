# first of all import the socket library
import socket
import json, time
import os, sys
import datetime

from pymongo import MongoClient
from pprint import pprint


# serverStatusResult = db.command("serverStatus")
socket = socket.socket()
port = int(sys.argv[1])

socket.bind(('', port))
print("Socket is created with port %s" % port)

socket.listen(5)
print("Listening")

i = 0
while True:
    connection, address = socket.accept()
    print "Got Connected with ", address

    i = i+1
    start_time = time.time()
    child_pid = os.fork()
    if child_pid == 0:
        print "Process",address
        print i
        socket.close()
        while True:

            data = connection.recv(2049)
            yo = "yo"
            if data == "read":
                lines = open('wordfile.txt').read()
                data1 = json.dumps(lines)
                connection.send(data1)
                yo = connection.recv(4098)
            if data == "write" or yo == "write":
                lines = open('wordfile.txt', 'a')
                change = connection.recv(4098)
                client = MongoClient("mongodb://priyagup:Codepri%40143@advancedropboxproject-shard-00-00-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-01-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-02-jdfx8.mongodb.net:27017/test?ssl=true&replicaSet=AdvanceDropboxproject-shard-0&authSource=admin&retryWrites=true")
                # db = client.admin
                db = client["AdvanceDropboxproject"]
                col = db["History"]
                i = address
                now = datetime.datetime.now()
                lis = {"port": i, "Time": str(now)}
                x = col.insert_one(lis)
                # print(x)
                # print(yo)
                lines.write(change)
            if data == "update":
                client = MongoClient("mongodb://priyagup:Codepri%40143@advancedropboxproject-shard-00-00-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-01-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-02-jdfx8.mongodb.net:27017/test?ssl=true&replicaSet=AdvanceDropboxproject-shard-0&authSource=admin&retryWrites=true")
                # db = client.admin
                db = client["AdvanceDropboxproject"]
                col = db["History"]
                for x in col.find():
                    print(x)
                    print(x.encode())
                    connection.send(x.encode())

                lines.close()
            break
            #
            # now = datetime.datetime.now()
            # lis = {"port": i, "Time": str(now)}
            # x = col.insert_one(lis)
            # array_of_word = []

            # for words in data.split(","):
            #     array_of_word.append(words)
            # result = mergeSort(array_of_word)

            # # if not data:
            # #     break
            # print i
        os._exit(0)
    print "child pid is %d" % child_pid

c.close()

