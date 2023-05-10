# Servidor TCP
import socket

# Dicionário de traduções
traducoes = {
    'rede': 'network',
    'roteador': 'router',
    'protocolo': 'protocol',
    'pacote': 'packet',
    'firewall': 'firewall',
    'DNS': 'DNS',
    'IP': 'IP',
    'cliente': 'client',
    'servidor': 'server',
    'conexão': 'connection'
}

# Configurações do servidor
HOST = 'localhost'  # Endereço IP do servidor
PORT = 5000  # Porta para conexão

# Cria o socket TCP
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

print(f"Servidor TCP aguardando conexões na porta {PORT}...")

while True:
    # Aguarda uma conexão
    conn, addr = sock.accept()
    print(f"Conexão estabelecida com {addr[0]}:{addr[1]}")

    # Recebe a palavra do cliente
    palavra = conn.recv(1024).decode()
    print(f"Palavra recebida do cliente: {palavra}")

    # Traduz a palavra, se existir no dicionário
    traducao = traducoes.get(palavra.lower(), 'Palavra não encontrada')

    # Envia a tradução para o cliente
    conn.sendall(traducao.encode())

    # Encerra a conexão com o cliente
    conn.close()