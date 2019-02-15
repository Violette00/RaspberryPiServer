import socket

s = socket.socket()
host = "192.168.1.123"
port = 63947

s.connect((host, port))
s.send("Hello Server!")

with open('received_file', 'wb') as f:
    print("File Opened")
    while True:
        print("Receiving data...")
        data = s.recv(1024)
        print ("data=%s", (data))
        if not data:
            break
        f.write(data)

f.close()
print("Successfully got the file")
s.close()
print("Connection Closed")