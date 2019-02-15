import socket

port = 60000
s = socket.socket()
host = socket.gethostname()
s.bind((host, port))

print("Server Listening...")

while True:
    conn, addr = s.accept()
    print("Got Connection from ", addr)
    data = conn.recv(1024)
    print("Server Received ", repr(data))
    filename = "mytxt.txt"
    f = open(filename, 'rb')
    l = f.read(1024)
    while (l):
        conn.send(l)
        print("Sent ", repr(l))
        l = f.read(1024)
    f.close()

    print("Done Sending!")
    conn.send("Thank you for connecting!")
    conn.close()