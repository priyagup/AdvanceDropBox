
# first of all import the socket library 
import socket
import json, pickle
import os, sys, datetime    
from pymongo import MongoClient
# next create a socket object 
class socketProgram(object):
    def __init__(self):
        #self.data = []
        self.flag =0
    

    def main(self):
        s = socket.socket()          
        print "Socket successfully created"
        port = int(sys.argv[1])
        s.bind(('', port))         
        print "socket binded to %s" %(port) 
          
        # put the socket into listening mode 
        s.listen(5)      
        print "socket is listening"
        while True: 
            # Establish connection with client. 
            connection, addr = s.accept()      
            print 'Got connection from', addr 
            print(self.flag)
            pid=os.fork()
            if (pid)==0:
                print "New child created for client request"
                s.close()
                # send a thank you message to the client.  
                #Echo code
                while True:
                    data = connection.recv(2048)
                    if data == "read":
                        lines = open('wordfile.txt').read()
                        data1 = json.dumps(lines)
                        connection.send(data1)
                    if data == "write":
                        self.flag =1
                        print(self.flag)
                        lines = open('wordfile.txt', 'a')
                        change = connection.recv(4096)
                        client = MongoClient("mongodb://priyagup:Codepri%40143@advancedropboxproject-shard-00-00-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-01-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-02-jdfx8.mongodb.net:27017/test?ssl=true&replicaSet=AdvanceDropboxproject-shard-0&authSource=admin&retryWrites=true")
                        
                        db = client["AdvanceDropboxproject"]
                        col = db["History"]
                        i = addr
                        now = datetime.datetime.now()
                        lis = {"port": i, "Time": str(now)}
                        x = col.insert_one(lis)
                        # print(x)
                        # print(yo)
                        lines.write(change)
                    if data == "update":
                        client = MongoClient("mongodb://priyagup:Codepri%40143@advancedropboxproject-shard-00-00-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-01-jdfx8.mongodb.net:27017,advancedropboxproject-shard-00-02-jdfx8.mongodb.net:27017/test?ssl=true&replicaSet=AdvanceDropboxproject-shard-0&authSource=admin&retryWrites=true")
                        
                        db = client["AdvanceDropboxproject"]
                        col = db["History"]
                        for x in col.find():
                            print(x)
                            print(x.encode())
                            connection.send(x.encode())

                        lines.close()
                    if data == "4":
                        break
if __name__== "__main__":
    socketProgram().main()


	
	
# Close the connection with the client 
c.close()