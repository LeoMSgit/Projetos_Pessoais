def calcular_polinomio(coeficientes, x):
    grau = len(coeficientes) - 1
    resultado = 0
    for i in range(grau + 1):
        resultado += coeficientes[i][0] * (x ** (grau - i))
    return resultado

def obter_coeficientes():
    grau = int(input("Digite o grau do polinômio: "))
    coeficientes = []
    for i in range(grau + 1):
        coeficiente = float(input(f"Digite o coeficiente para x^{grau - i}: "))
        coeficientes.append((coeficiente,))
    return coeficientes

def imprimir_funcao(coeficientes):
    print("A função inserida é:")
    funcao = ""
    grau = len(coeficientes) - 1
    for i in range(grau + 1):
        coeficiente, = coeficientes[i]
        termo = f"{coeficiente}x^{grau - i}" if coeficiente != 1 else f"x^{grau - i}"
        funcao += termo
        if i != grau:
            funcao += " + "
    print(funcao)

def main():
    print("Bem-vindo à Calculadora de Polinômios")
    print("--------------------------------------")
    coeficientes = obter_coeficientes()
    imprimir_funcao(coeficientes)
    opcao = input("Esta é a função que você deseja calcular? (s/n): ")
    if opcao.lower() == "s":
        x = float(input("Digite o valor de x para calcular o polinômio: "))
        resultado = calcular_polinomio(coeficientes, x)
        print(f"O resultado para x = {x} é: {resultado}")
    else:
        print("Operação cancelada.")

if __name__ == "__main__":
    main()
