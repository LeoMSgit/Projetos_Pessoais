Passo 2 - Envio de Dados Pessoais
Objetivo: Enviar seus dados em formato JSON e receber uma questão lógica.

Endpoint: POST https://desafio-endpoint-hashcode-n2.onrender.com/passo2

Solução: Utilizar o site https://hoppscotch.io/


Corpo (JSON):
```json
{
  "cpf": "123.456.789-09"
}
```
Resultado:
```json
{
  "status": 201,
  "mensage": "Parabéns, você concluiu o Passo 2!",
  "description": "No passo 3 realize uma requisição do tipo POST no endpoint: https://desafio-endpoint-hashcode-n2.onrender.com/passo3",
  "recomendations": "Envie no corpo da requisição seu cpf e a resposta da pergunta objetiva no seguinte formato: {cpf:xxx.xxx.xxx-xx, respostaQuestaoObjetiva: xxxxxxxx}, Atenção: a resposta da questão é pequena, sendo uma palavra ou um número informado como string",
  "objectiveQuestion": "PO5Q - Qual é o valor da variável resultado se resultado = 2^3 + 5?"
}
```
