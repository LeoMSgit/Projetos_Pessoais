def calcular_polinomio(coeficientes, x):
    grau = len(coeficientes) - 1
    resultado = 0
    for i in range(grau + 1):
        resultado += coeficientes[i] * (x ** (grau - i))
    return resultado

def obter_coeficientes():
    grau = int(input("Digite o grau do polinômio: "))
    coeficientes = []
    for i in range(grau + 1):
        coeficiente = float(input("Digite o coeficiente para x^{}: ".format(grau - i)))
        coeficientes.append(coeficiente)
    return coeficientes

def main():
    print("Bem-vindo à Calculadora de Polinômios")
    print("--------------------------------------")
    coeficientes = obter_coeficientes()
    x = float(input("Digite o valor de x para calcular o polinômio: "))
    resultado = calcular_polinomio(coeficientes, x)
    print("O resultado para x = {} é: {}".format(x, resultado))

if __name__ == "__main__":
    main()
