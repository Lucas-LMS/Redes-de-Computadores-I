# Cliente TCP
import socket

# Configurações do servidor
HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta para conexão

# Cria o socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
sock.connect((HOST, PORT))

# Solicita a palavra ao usuário
palavra = input("Digite a palavra em português: ")

# Envia a palavra para o servidor
sock.sendall(palavra.encode())

# Recebe a tradução do servidor
traducao = sock.recv(1024).decode()

print(f"A tradução para inglês é: {traducao}")

# Encerra a conexão com o servidor
sock.close()