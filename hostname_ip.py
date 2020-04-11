import socket

hostname = (input("Insira o Hostname: "))
addr = socket.gethostbyname(hostname)
print(f'O Ip do Host digitado é {addr}')

