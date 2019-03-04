# first of all import the socket library
import socket
import json, time
import os, sys

from pymongo import MongoClient
from pprint import pprint
client = MongoClient("mongodb://priyagup:Codepri%40143@advancedropboxproject-shard-00-00-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-01-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-02-jdfx8.mongodb.net:27017/test?ssl=true&replicaSet=AdvanceDropboxproject-shard-0&authSource=admin&retryWrites=true")
db = client.admin

serverStatusResult = db.command("serverStatus")
pprint(serverStatusResult)

def mergeSort(array_of_word):
    if len(array_of_word) > 1:
		mid = len(array_of_word) // 2
		L = array_of_word[:mid]
		R = array_of_word[mid:]
		mergeSort(L)
		mergeSort(R)
		i = j = k = 0
		while i < len(L) and j < len(R):
			if L[i] < R[j]:
				array_of_word[k] = L[i]
				i += 1
			else:
				array_of_word[k] = R[j]
				j += 1
			k += 1
			while i < len(L):
				array_of_word[k] = L[i]
				i += 1
				k += 1
			while j < len(R):
				array_of_word[k] = R[j]
				j += 1
				k += 1
    return array_of_word

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
    i=i+1
    start_time = time.time()
    child_pid = os.fork()
    if (child_pid) == 0:
        print "Process",address
        print i
        socket.close()
        while True:
            data = connection.recv(2049)
            array_of_word = []
            for words in data.split(","):
                array_of_word.append(words)
            result = mergeSort(array_of_word)
            data1 = json.dumps(result)
            if not data:
                break
            print i
            connection.send(data1.strip())
        os._exit(0)
    print "child pid is %d" % (child_pid)

c.close()
