import random

def gerar_placa():
    """Gera uma placa de veículo brasileira aleatória."""

    letras = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))     # Gera 3 letras aleatórias
    numeros = ''.join(random.choices('0123456789', k=4))                    # Gera 4 números aleatórios

    placa = f"{letras}-{numeros}"                                           # Formato da placa: LLL-NNNN (onde L é letra e N é número)
    return placa

for _ in range(5):                                                          # Gera 5 placas
    print(gerar_placa())
