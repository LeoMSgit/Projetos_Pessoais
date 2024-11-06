from datetime import datetime
from dateutil.relativedelta import relativedelta
from twilio.rest import Client
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados de configuração do Twilio
ACCOUNT_SID = 'SEU_ACCOUNT_SID_AQUI'
AUTH_TOKEN = 'SEU_AUTH_TOKEN_AQUI'
TWILIO_WHATSAPP_NUMBER = 'whatsapp:+1415XXXXXXX'  # Número do Twilio
MY_WHATSAPP_NUMBER = 'whatsapp:+55NUMERO_DE_DESTINO'  # Meu número de WhatsApp (não será usado diretamente, pois qualquer número pode interagir)

# Função que calcula a diferença de tempo e retorna a mensagem
def calcular_diferença():
    dataInicial = datetime(2019, 10, 21)
    dataAtual = datetime.now()

    dif = relativedelta(dataAtual, dataInicial)

    anos = dif.years
    meses = dif.months
    dias = dif.days

    return f"❤️  Feliz {anos} anos, {meses} meses e {dias} dias de namoro ❤️"

# Função que envia a resposta via WhatsApp usando Twilio
def enviar_resposta(mensagem, to_number):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body=mensagem,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=to_number
    )
    return message.sid

# Rota para receber mensagens
@app.route("/webhook", methods=["POST"])
def webhook():
    # Recupera o número do remetente e a mensagem
    from_number = request.values.get('From', '')
    body = request.values.get('Body', '').strip().lower()

    # Se a mensagem for "calcular namoro" ou algo relacionado, responde com o cálculo
    if "calcular namoro" in body:
        resposta = calcular_diferença()
        enviar_resposta(resposta, from_number)
        return jsonify({"status": "success"}), 200

    # Caso a mensagem não seja o comando, não fazer nada ou enviar uma resposta padrão.
    return jsonify({"status": "success"}), 200

if __name__ == "__main__":
    app.run(debug=True)
