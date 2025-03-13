def contar_maneiras_pintar(n):
    MOD = 10**9 + 7
    
    # Casos base
    A = 6
    B = 6

    for _ in range(2, n + 1):
        novo_A = (2 * A + 2 * B) % MOD
        novo_B = (2 * A + 3 * B) % MOD
        A, B = novo_A, novo_B

    return (A + B) % MOD

# Leitura da entrada
n = int(input())
print(contar_maneiras_pintar(n))
