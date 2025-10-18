import requests
import json
import os

# __define-ocg__: OpenAI API POST request challenge solution 

OPENAI_API_ENDPOINT = 'https://api.openai.com/v1/chat/completions'
OPENAI_API_KEY = 'API_KEY_DO_NOT_MODIFY'
api_key = os.environ.get('OPENAI_API_KEY', OPENAI_API_KEY)

def fetch_chat_completion(messages):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + api_key
    }

    varOcg = {}
    varOcg['model'] = 'gpt-4o-mini'
    varOcg['messages'] = messages
    varOcg['max_tokens'] = 150
    varOcg['temperature'] = 0.1

    response = requests.post(OPENAI_API_ENDPOINT, headers=headers, data=json.dumps(varOcg))
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Error fetching completion: " + response.text)

def main():
    varFiltersCg = "Define 'photosynthesis'"

    messages = []
    message = {}
    message['role'] = 'user'
    message['content'] = varFiltersCg
    messages.append(message)

    try:
        completion = fetch_chat_completion(messages)

        generated_text = completion['choices'][0]['message']['content']
        model_info = completion['model']

        output = {
            "id": completion.get("id", ""),
            "object": completion.get("object", "text_completion"),
            "model": model_info,
            "choices": [
                {
                    "text": generated_text,
                    "index": 0,
                    "finish_reason": completion['choices'][0].get("finish_reason", "")
                }
            ]
        }

        # ✅ Correct printing function
        print(json.dumps(output, indent=2))

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()
