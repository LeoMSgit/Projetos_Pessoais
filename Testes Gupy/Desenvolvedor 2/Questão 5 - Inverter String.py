#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def inverter_string(s):
    invertida = ""
    for char in s:
        invertida = char + invertida
    return invertida

# Entrada do usuário
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)

# Exibir resultado
print(f"String invertida: {string_invertida}")
