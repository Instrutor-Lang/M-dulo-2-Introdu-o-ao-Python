# primeiro_programa.py
print("Olá, mundo!")

# variaveis_tipos.py
nome = "Maria"
idade = 25
altura = 1.68
estudante = True

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Estudante: {estudante}")

# manipulacao_strings.py
mensagem = "  Python é divertido!  "
print(mensagem.strip())
print(mensagem.lower())

# input_usuario.py
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

# desafio_hora_atual.py
from datetime import datetime

nome = input("Qual é o seu nome? ")
agora = datetime.now()
hora_atual = agora.strftime("%H:%M")
print(f"Olá, {nome}! Agora são {hora_atual}.")

# programa_personalizado.py
from datetime import datetime

nome = input("Qual é o seu nome? ")
agora = datetime.now()
hora_atual = agora.strftime("%H:%M")
print(f"Olá, {nome}! Agora são {hora_atual}.")
