# Cliente UDP
import socket

# Configurações do servidor
HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta para conexão

# Cria o socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    # Solicita a palavra ao usuário
    palavra = input("Digite a palavra em português: ")

    # Envia a palavra para o servidor
    sock.sendto(palavra.encode(), (HOST, PORT))

    # Recebe a tradução do servidor
    data, address = sock.recvfrom(1024)
    traducao = data.decode()

    print(f"A tradução para inglês é: {traducao}")