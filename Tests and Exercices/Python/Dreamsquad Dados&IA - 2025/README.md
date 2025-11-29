# Case: API de Chat com Agente de IA (dreamsquad)

## Chat Agent com Ollama, FastAPI e Tool de Cálculo


Este projeto implementa uma API simples que conecta um agente de IA a um modelo local rodando via Ollama. O agente reconhece quando a pergunta e um cálculo e usa uma tool para resolver. Para perguntas gerais, delega ao LLM.


### Requisitos

- Python 3.10 ou superior
- Ollama instalado localmente


### Instalação

1. Clone o repositório
```bash
git clone <seu-repo>
cd project
```

2. Crie e ative um ambiente virtual
```
python -m venv venv
source venv/bin/activate # no Windows use venv\Scripts\activate
```

3. Instale dependencias
```
pip install -r requirements.txt
```

4. Configure vari[aveis de ambiente
```
Copie .env.example para .env e ajuste OLLAMA_MODEL conforme o modelo instalado localmente.
```

5. Instale e configure o Ollama
Siga as instrucoes oficiais do Ollama para instalar em seu sistema. Depois de instalado, verifique se o comando ollama funciona no terminal e se voce possui um modelo local carregado. O projeto tenta usar o CLI ollama run <model> "prompt" como fallback.

### Execução
```
uvicorn main:app --reload
```
Endpoint:

POST /chat

payload: { "message": "Seu texto" }

resposta: { "response": "texto do agente" }

### Observações

O codigo tenta importar o Strands Agents SDK. Se o SDK estiver instalado, o projeto registrara uma tool usando a API do SDK. Se nao estiver, o projeto usa um fallback que chama o Ollama via CLI e usa a tool implementada em tools.py para calculos.

Se for necessario ajustar a chamada ao Ollama (por exemplo, usar a API HTTP), atualize agent._call_ollama_cli para usar requests para OLLAMA_HOST.
