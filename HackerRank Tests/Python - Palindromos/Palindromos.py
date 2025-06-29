lista = ["bat", "tab", "cat", "tac", "lol", "today", "roma", "amor", "mora"]
lista1 = []  # Pares encontrados (ex: "bat" e "tab")
lista2 = []  # Palavras que não têm par reverso
resposta = []

def func():
    usados = set()
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j][::-1]:
                lista1.append((lista[i], lista[j]))
                usados.add(lista[i])
                usados.add(lista[j])

    for word in lista:
        if word not in usados:
            lista2.append(word)

    resposta.append(lista1)
    resposta.append(lista2)

func()
print(resposta)
