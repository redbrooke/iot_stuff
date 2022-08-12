import socket
import threading

s = socket.socket() 
s.bind(('0.0.0.0', 3800 ))
s.listen(0)
current = 0
split = []

while True:
    client, addr = s.accept()
    while True:
        content = client.recv(32)
        if len(content) ==0:
           break
        else:
            print(content)
            storage = open("output.txt", "a")
	    split = content.split(":")
	    storage.write('{' + ','.join(split) + '}' + ',' + "\n")
	    storage.close()

print("Closing connection")
client.close()
