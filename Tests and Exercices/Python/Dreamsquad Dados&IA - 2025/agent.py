import os
import re
import subprocess
import json
from typing import Optional


from tools import calculate


# tentativa de importar Strands Agents. Se disponivel, construimos o agente com a API do SDK.
try:
from strands.agents import Agent as StrandsAgent, Tool as StrandsTool
STRANDS_AVAILABLE = True
except Exception:
STRANDS_AVAILABLE = False




def _detect_math_question(text: str) -> Optional[str]:
# padrao simples: se conter apenas numeros, operadores e funcoes sqrt/pow, considera calculo
math_like = re.search(r"[0-9\)\(]+\s*([\+\-\*\/\%\^]|\*\*)\s*[0-9]", text)
word_math = re.search(r"raiz|sqrt|calcule|quanto é|quanto e|quanto é|quanto sao|quanto são", text.lower())
if math_like or word_math:
return text
return None




class ChatAgent:
def __init__(self):
self.model = os.getenv('OLLAMA_MODEL', 'llama2')
self.ollama_host = os.getenv('OLLAMA_HOST', 'http://localhost:11434')
# se Strands estiver disponivel, instancia a tool
if STRANDS_AVAILABLE:
self._init_strands_agent()
else:
self._init_fallback_agent()


def _init_strands_agent(self):
# exemplo genérico: registra uma tool que chama a função calculate
try:
def tool_func(args):
expr = args.get('expression') if isinstance(args, dict) else args
return calculate(expr)


calc_tool = StrandsTool(name='calculator', func=tool_func, description='Tool para calculos matematicos')
self.agent = StrandsAgent(model=self.model, tools=[calc_tool])
self.use_strands = True
except Exception:
# se falhar, fallback
self._init_fallback_agent()


def _init_fallback_agent(self):
# fallback: agente leve que decide quando usar a tool e quando consultar Ollama via CLI
self.use_strands = False


def _call_ollama_cli(self, prompt: str) -> str:
# tenta chamar o CLI do ollama se estiver no PATH
return response
