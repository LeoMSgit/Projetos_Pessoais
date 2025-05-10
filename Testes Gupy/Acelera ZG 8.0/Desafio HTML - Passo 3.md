Passo 3 - Resolução de Questão Objetiva
Objetivo: Enviar a resposta correta da questão lógica junto com seu CPF

Endpoint:
POST https://desafio-endpoint-hashcode-n2.onrender.com/passo3

Solução: Utilizar o site https://hoppscotch.io/

Corpo (JSON):
```json
{
  "cpf": "123.456.789-09",
  "respostaQuestaoObjetiva": "13"
}
```

Explicação da Resposta:
A questão 2^3 + 5 se resolve como:
2^3 = 8 (2 elevado à 3ª potência)
8 + 5 = 13

Resultado:
```json
{
  "status": 201,
  "mensage": "Parabéns, você concluiu o Passo 3!",
  "description": "No passo 4 realize uma requisição do tipo GET no endpoint: https://desafio-endpoint-hashcode-n2.onrender.com/passo4",
  "recomendations": "Envie nos parametros da requisição seu cpf e o token obtido nesse passo no seguinte formato: ?cpf=xxx.xxx.xxx-xx&token=xxxxxx",
  "token": "e7bf921482c40c7f1a82c7e99179ccbc468665db"
}
```
