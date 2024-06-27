

import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
buffer_size = 1024
#need to allow external ips, not simply local host/local machine ips
host =''
port = 9879
mysocket.bind((host, port))
mysocket.listen(5)
(client, (ip,port)) = mysocket.accept()
print(client, port)
client.send(b"knock knock knock, I'm the server")
data = client.recv(buffer_size)
print(data.decode())
mysocket.close()
