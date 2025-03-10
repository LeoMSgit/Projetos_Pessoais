#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;import json

# Simulação de um JSON contendo o faturamento diário
dados_faturamento_json = '''{
    "faturamento": [1000, 2000, 0, 3000, 2500, 0, 4000,
                    5000, 0, 6000, 7000, 0, 8000, 9000,
                    0, 10000, 11000, 0, 12000, 13000, 0]
}'''

# Carregar os dados do JSON
dados = json.loads(dados_faturamento_json)
valores = [valor for valor in dados["faturamento"] if valor > 0]  # Ignora dias sem faturamento

# Cálculos
menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_faturamento = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media_faturamento)

# Exibir resultados
print(f"Menor faturamento: {menor_faturamento}")
print(f"Maior faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
