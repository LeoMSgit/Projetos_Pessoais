def groupSort(arr):
    # Conta as ocorrências de cada elemento usando um dicionário
    contagem = {}
    for val in arr:
        contagem[val] = contagem.get(val, 0) + 1
    
    # Cria uma lista de pares [valor, quantidade]
    resposta = [[val, count] for val, count in contagem.items()]
    
    # Ordena pela quantidade (desc), e pelo valor (asc) se quantidades iguais
    resposta.sort(key=lambda x: (-x[1], x[0]))
    
    return resposta
