while True:
    try:
        celsius = float(input())

        if 0 <= celsius <= 1000:
            break
        else:
            print("Valor inválido! Digite uma temperatura entre 0 e 1000.")
    except ValueError:
        print("Entrada inválida! Digite um número válido.")

kelvin = celsius + 273.15
fahrenheit = celsius * 1.80 + 32.00

print("{:.5f}, {:.5f}".format(kelvin, fahrenheit))
