# Servidor UDP
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

# Cria o socket UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

print(f"Servidor UDP aguardando conexões na porta {PORT}...")

while True:
    # Recebe a palavra do cliente
    data, address = sock.recvfrom(1024)
    palavra = data.decode()

    print(f"Palavra recebida do cliente: {palavra}")

    # Traduz a palavra, se existir no dicionário
    traducao = traducoes.get(palavra.lower(), 'Palavra não encontrada')

    # Envia a tradução para o cliente
    sock.sendto(traducao.encode(), address)