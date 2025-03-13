def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

def soma_fatoriais(numeros):
    soma = 0
    for numero in numeros:
        soma += fatorial(numero)
    return soma

N = int(input())
numeros = list(map(int, input().split()))

if len(numeros) != N:
    print("Número inválido de entradas.")
else:
    print(soma_fatoriais(numeros))
