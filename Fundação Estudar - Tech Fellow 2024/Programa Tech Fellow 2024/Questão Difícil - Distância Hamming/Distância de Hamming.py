def hamming_distance(x, y):
    # Convertendo para representação binária
    binary_x = bin(x)[2:]
    binary_y = bin(y)[2:]

    # Completando com zeros à esquerda para terem o mesmo comprimento
    max_len = max(len(binary_x), len(binary_y))
    binary_x = binary_x.zfill(max_len)
    binary_y = binary_y.zfill(max_len)

    # Calculando a distância de Hamming
    hamming_dist = sum(bit_x != bit_y for bit_x, bit_y in zip(binary_x, binary_y))
    return hamming_dist

# Entrada
x, y = map(int, input().split())

# Calculando e imprimindo a distância de Hamming
print(hamming_distance(x, y))
