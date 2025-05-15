# Importação Bibliotecas
import requests
from bs4 import BeautifulSoup
import base64
import json
from IPython.display import display, Image
import re

# Configurações
BASE_URL = "https://intern.aiaxuropenings.com"
SCRAPE_URL = f"{BASE_URL}/scrape/3c6b886f-18a2-4954-a6d2-db207221645b"
API_URL = f"{BASE_URL}/v1/chat/completions"
SUBMIT_URL = f"{BASE_URL}/api/submit-response"
TOKEN = "nkpjAc191po9eDVkos29aIyA626V6Qun"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

# Download da imagem
def download_image():
    print("Acessando página para download da imagem...")
    try:
        response = requests.get(SCRAPE_URL, headers=headers, timeout=15)
        response.raise_for_status()
        
        print("Analisando conteúdo da página...")
        
        # Procurar por imagem codificada em base64
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Padrão para encontrar imagens base64
        base64_pattern = re.compile(r'data:image\/[^;]+;base64,([^\"]+)')
        matches = base64_pattern.findall(response.text)
        
        if matches:
            print(f"Encontradas {len(matches)} imagens em base64")
            img_data = base64.b64decode(matches[0])
            with open("downloaded_image.jpg", "wb") as f:
                f.write(img_data)
            display(Image(img_data))
            return img_data

        response.close()
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar a página: {e}")
        return None


# Processar imagem
def process_image(img_data):
    # Envia a imagem para a API de inferência e retorna a resposta
    try:
        if not img_data:
            raise ValueError("Dados da imagem vazios")

        encoded_image = base64.b64encode(img_data).decode('utf-8')

        payload = {
            "model": "microsoft-florence-2-large",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{encoded_image}"
                            }
                        },
                        {
                            "type": "text",
                            "text": "<DETAILED_CAPTION>"
                        }
                    ]
                }
            ],
            "max_tokens": 300
        }

        print("Enviando imagem para processamento...")
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()

        api_response = response.json()
        print("✅ Resposta da API recebida com sucesso!")
        return api_response

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na requisição à API: {e}")
        if 'response' in locals():
            print(f"Resposta da API: {response.text}")
        return None
    except Exception as e:
        print(f"❌ Erro ao processar imagem: {e}")
        return None

# Submeter resposta
def submit_response(api_response):
    # Submete a resposta da API para o endpoint de avaliação
    try:
        if not api_response or not isinstance(api_response, dict):
            raise ValueError("Resposta da API inválida")

        print("\nSubmetendo resposta para avaliação...")
        response = requests.post(SUBMIT_URL, headers=headers, json=api_response, timeout=10)
        response.raise_for_status()

        result = response.json()
        print("✅ Resposta submetida com sucesso!")
        print(f"Resultado: {result}")
        return result

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao submeter resposta: {e}")
        if 'response' in locals():
            print(f"Resposta do servidor: {response.text}")
        return None
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return None

# Main
def main():
    print("Iniciando processo de avaliação técnica...\n")

    # 1. Download da imagem
    image_data = download_image()
    if not image_data:
        print("Falha no download da imagem. Abortando...")
        return

    # 2. Processamento da imagem
    api_response = process_image(image_data)
    if not api_response:
        print("Falha no processamento da imagem. Abortando...")
        return

    # 3. Submissão da resposta
    submission_result = submit_response(api_response)
    if not submission_result:
        print("Falha na submissão da resposta. Abortando...")
        return

    print("\nProcesso concluído com sucesso!")

if __name__ == "__main__":
    main()
