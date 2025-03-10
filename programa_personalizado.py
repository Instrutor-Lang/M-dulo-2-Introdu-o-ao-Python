from datetime import datetime

nome = input("Qual é o seu nome? ")
agora = datetime.now()
hora_atual = agora.strftime("%H:%M")
print(f"Olá, {nome}! Agora são {hora_atual}.")
