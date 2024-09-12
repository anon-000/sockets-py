import socket


targetIp = "127.0.0.1"
targetPort = 8888


soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket)

soc.bind((targetIp, targetPort))
print(f"Listening to : {targetIp}:{targetPort}")
soc.listen(1)



