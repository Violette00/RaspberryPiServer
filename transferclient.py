import socket

s = socket.socket()
host = "192.168.1.123"
port = 63947

s.connect((host, port))

filename = "Moneyball.2011.720p.BrRip.x264.YIFY.mp4"
f = open(filename, 'rb')
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
f.close()

print ("Done Sending")
s.close()
print("Connection Closed")