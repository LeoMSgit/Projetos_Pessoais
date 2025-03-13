# your code goes here
while True:
    celsius = float(input("Digite a temperatura em Celsius: "))

    if 0 <= celsius <= 1000:
        break
    else:
        print("Valor inválido! Digite uma temperatura entre 0 e 1000.")

kelvin = celsius + 273.15
fahrenheit = celsius * 1.80 + 32.00

print(f"{kelvin:.5f}, {fahrenheit:.5f}")
