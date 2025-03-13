Conversão de Temperatura
Descrição do Problema
Imagine um número decimal não negativo, com até duas casas decimais, que representa a temperatura em graus Celsius. Sua tarefa é converter essa temperatura para Kelvin e Fahrenheit e retornar os resultados em uma lista no seguinte formato: ans = [kelvin, fahrenheit].

Fórmulas para Conversão
Kelvin: Kelvin = Celsius + 273.15
Fahrenheit: Fahrenheit = Celsius × 1.80 + 32.00
Exemplos
Exemplo 1
Input	Output
36.50	309.65000, 97.70000
Explicação:

36.50 °C em Kelvin = 309.65000
36.50 °C em Fahrenheit = 97.70000
Exemplo 2
Input	Output
122.11	395.26000, 251.79800
Explicação:

122.11 °C em Kelvin = 395.26000
122.11 °C em Fahrenheit = 251.79800
Restrições e Requisitos
Garanta que a entrada está dentro do intervalo permitido: 0 ≤ celsius ≤ 1000
Os valores retornados em Kelvin e Fahrenheitdevem conter 5 casas decimais cada.
O usuário deve dar o input dos dados (no caso, o sistema dará o input de 5 testes de casos e usará o output para conferir seus acertos).
Observações
As casas decimais dos números neste problema estão sendo representadas por ponto e não por vírgula.
O output não deve estar seguido das unidades de medida e não precisa estar entre [ ], somente dos números e separados por vírgulas, exatamente como nos exemplos.
