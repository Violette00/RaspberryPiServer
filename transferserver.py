import socket

port = 63947
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.123"
print("Host: ", host)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(1)

print("Server Listening...")

while True:
    conn, addr = s.accept()
    print("Got Connection from ", addr)
#    data = conn.recv(1024)
#   print("Server Received ", repr(data))
    with open("Moneyball.mp4", 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)

    f.close()

    #vvv file sending code
    #filename = "mytxt.txt"
    #f = open(filename, 'rb')
    #l = f.read(1024)
    #while (l):
     #   conn.send(l)
     #   print("Sent ", repr(l))
     #   l = f.read(1024)
    #f.close()

    print("Done Sending!")
    conn.send("File Received")
    conn.close()