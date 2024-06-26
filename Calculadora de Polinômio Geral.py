def calcular_polinomio(coeficientes, x):
    grau = len(coeficientes) - 1
    resultado = 0
    for i in range(grau + 1):
        resultado += coeficientes[i][0] * (x ** (grau - i))
    return resultado

def obter_coeficientes():
    while True:
        entrada = input("Digite o grau do polinômio ou EXIT para SAIR: ")
        if entrada.lower() == 'exit':
            return None
        try:
            grau = int(entrada)
            if grau < 0:
                print("O grau do polinômio deve ser um número inteiro não negativo.")
                continue
            break
        except ValueError:
            print("Por favor, digite um número inteiro para o grau.")

    coeficientes = []
    for i in range(grau + 1):
        while True:
            try:
                coeficiente = float(input("Digite o coeficiente para x^{}: ".format(grau - i)))
                break
            except ValueError:
                print("Por favor, digite um número válido para o coeficiente.")
        coeficientes.append((coeficiente,))
    return coeficientes

def imprimir_funcao(coeficientes):
    print("A função inserida é:")
    funcao = ""
    grau = len(coeficientes) - 1
    for i in range(grau + 1):
        coeficiente, = coeficientes[i]
        termo = "{}x^{}".format(coeficiente, grau - i) if grau - i != 0 else "{}".format(coeficiente)
        funcao += termo
        if i != grau:
            funcao += " + "
    print(funcao)

def main():
    while True:
        print("Bem-vindo à Calculadora de Polinômios")
        print("--------------------------------------")
        coeficientes = obter_coeficientes()
        if coeficientes is None:
            print("Saindo...")
            break
        imprimir_funcao(coeficientes)
        while True:
            opcao = input("Deseja calcular o polinômio? (s/n): ").lower()
            if opcao in ['s', 'n']:
                break
            else:
                print("Opção inválida. Por favor, digite 's' para sim ou 'n' para não.")

        if opcao == "s":
            x = float(input("Digite o valor de x para calcular o polinômio: "))
            resultado = calcular_polinomio(coeficientes, x)
            print("O resultado para x = {} é: {}".format(x, resultado))
        else:
            print("Operação cancelada... retornando para o Menu")
            print()
            print()
if __name__ == "__main__":
    main()
