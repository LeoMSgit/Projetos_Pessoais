import ast
import operator as op
import math


# operadores permitidos
ALLOWED_OPERATORS = {
ast.Add: op.add,
ast.Sub: op.sub,
ast.Mult: op.mul,
ast.Div: op.truediv,
ast.Pow: op.pow,
ast.USub: op.neg,
ast.Mod: op.mod,
}


def _eval(node):
if isinstance(node, ast.Num): # <number>
return node.n
if isinstance(node, ast.Constant):
return node.value
if isinstance(node, ast.BinOp):
left = _eval(node.left)
right = _eval(node.right)
op_type = type(node.op)
if op_type in ALLOWED_OPERATORS:
return ALLOWED_OPERATORS[op_type](left, right)
raise ValueError(f"Operador nao permitido: {op_type}")
if isinstance(node, ast.UnaryOp):
operand = _eval(node.operand)
op_type = type(node.op)
if op_type in ALLOWED_OPERATORS:
return ALLOWED_OPERATORS[op_type](operand)
raise ValueError(f"Operador unario nao permitido: {op_type}")
if isinstance(node, ast.Call):
# permite apenas math.sqrt e pow via nomes simples
if isinstance(node.func, ast.Attribute):
if getattr(node.func, 'attr', None) == 'sqrt':
arg = _eval(node.args[0])
return math.sqrt(arg)
if isinstance(node.func, ast.Name):
if node.func.id == 'sqrt':
arg = _eval(node.args[0])
return math.sqrt(arg)
if node.func.id == 'pow':
a = _eval(node.args[0])
b = _eval(node.args[1])
return pow(a, b)
raise ValueError('Chamada de funcao nao permitida')
raise ValueError(f'No node para avaliar: {type(node)}')




def calculate(expression: str) -> str:
"""
Avalia expressões matemáticas simples de forma segura.
Suporta +, -, *, /, %, ** e sqrt(...).
Retorna string com resultado ou mensagem de erro.
"""
try:
# pre processamento: substitui 'raiz' por sqrt, aceita vírgula como ponto
expr = expression.lower().replace('raiz', 'sqrt').replace(',', '.')
# remove caracteres indesejados (mantém números, operadores, parênteses, letras para sqrt e pow)
# parsing por ast garante segurança
node = ast.parse(expr, mode='eval').body
result = _eval(node)
# tornar inteiro quando for inteiro
return f'Erro ao calcular: {e}'
