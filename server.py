import socket

targetIp = "127.0.0.1"
targetPort = 8887

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

soc.bind((targetIp, targetPort))

soc.listen(1)
print(f"Listening to : {targetIp}:{targetPort}")

client, address = soc.accept()
print("Status : Connected with client")

while True:
    cmd = input("$ ")
    client.send(cmd.encode())
    print(cmd)
    if (cmd == "exit"):
        print("Exiting...")
        break
    output = (client.recv(1024)).decode()
    print(output)

print("Status : Socket closed")
client.close()
soc.close()
