import socket, json
import time, sys
import random

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = sys.argv[1]
port = int(sys.argv[2])

s.connect((host, port))
open('clientinput.dat','w').close()
lines = open('wordfile.txt').read().splitlines()
file = open('clientinput.dat', 'a')

# Randomly generate 20 words from the line and store it into the array
for n in range(20):
    random.shuffle(lines)
    word = random.choice(lines)
    if n<19:	  
    	new_word = word + ","
    else:
	new_word = word     
    file.write(new_word)
file.write("\n")
for n in range(20):
    random.shuffle(lines)
    word = random.choice(lines)
    if n<19:	  
    	new_word = word + ","
    else:
	new_word = word
    file.write(new_word)
file.write("\n")
for n in range(20):
    random.shuffle(lines)
    word = random.choice(lines)
    if n<19:	  
    	new_word = word + ","
    else:
	new_word = word
    file.write(new_word)
file.close()


# opening a file
client_file = open('clientinput.dat').read().splitlines()
for x in client_file:
    time.sleep(2)
    s.send(x.strip().encode())
    data = s.recv(2048)
    data_arr = json.dumps(data)
    print(data_arr.replace("\\", ""))
s.close()
