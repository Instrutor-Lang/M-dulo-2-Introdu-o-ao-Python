Módulo 2: Introdução ao Python
Objetivo do Módulo
Neste módulo, os alunos serão introduzidos à linguagem Python, suas características e aplicações. Aprenderão a configurar o ambiente de desenvolvimento, escrever seus primeiros programas e entender conceitos básicos como variáveis e tipos de dados.

Estrutura da Aula
1. Introdução ao Python (20 minutos)
📌 O que é Python e por que é popular?
Linguagem de alto nível, fácil de aprender e muito versátil.
Aplicações: desenvolvimento web, ciência de dados, automação, machine learning, entre outras.
📌 Principais características do Python:
✅ Sintaxe simples e legível.
✅ Linguagem interpretada (execução linha por linha).
✅ Grande comunidade e vasta coleção de bibliotecas.

2. Instalação e Configuração do Ambiente (30 minutos)
📌 Instalando o Python
Windows: Download e instalação pelo site oficial.
Linux/Mac: Verificar a instalação com python3 --version e instalar, se necessário.
📌 Configurando o ambiente de desenvolvimento
Escolha do editor: VS Code ou PyCharm.
Configuração para rodar scripts Python.
📌 Testando a instalação
Abrir o terminal e digitar python ou python3 para acessar o interpretador Python.

3. Primeiros Passos no Python (40 minutos)
📌 O interpretador Python
Executando comandos diretamente no terminal.
Usando o interpretador como calculadora.
📌 Escrevendo o primeiro programa

print("Olá, mundo!")

📌 Executando um script Python

python nome_do_arquivo.py

📌 Trabalhando com variáveis e tipos de dados
✅ O que são variáveis e como atribuir valores?
✅ Principais tipos de dados:
int (números inteiros)
float (números decimais)
str (textos)
bool (valores booleanos)
📌 Exemplo:

nome = "Estevão"
idade = 30
altura = 1.75
estudante = True


4. Manipulação de Strings (30 minutos)
📌 O que são strings e como manipulá-las?
Concatenação de strings

saudacao = "Olá, " + nome + "!"

Métodos úteis de strings
upper(), lower(), strip(), replace(), split().
📌 Exemplo prático:

mensagem = "  Python é incrível!  "
print(mensagem.strip())  # Remove espaços em branco
print(mensagem.lower())  # Converte para minúsculas


5. Atividade Prática (40 minutos)
✅ Criar um programa que solicita o nome do usuário e exibe uma mensagem personalizada.
📌 Exemplo:

nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Bem-vindo ao curso de Python.")


6. Desafio Extra (20 minutos)
✅ Exibir a hora atual junto com a saudação.
📌 Usando a biblioteca datetime:

from datetime import datetime
agora = datetime.now()
hora_atual = agora.strftime("%H:%M")
print(f"Olá, {nome}! Agora são {hora_atual}.")


Exemplos de Código
📌 Primeiro Programa

print("Olá, mundo!")

📌 Variáveis e Tipos de Dados

nome = "Maria"
idade = 25
altura = 1.68
estudante = True

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Estudante: {estudante}")

📌 Manipulação de Strings

mensagem = "  Python é divertido!  "
print(mensagem.strip())  # Remove espaços em branco
print(mensagem.lower())  # Converte para minúsculas

📌 Programa com Input do Usuário

nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Bem-vindo ao curso de Python.")

📌 Desafio Extra: Hora Atual

from datetime import datetime
agora = datetime.now()
hora_atual = agora.strftime("%H:%M")
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Agora são {hora_atual}.")


Projeto Prático
📌 Descrição: Criar um programa que solicita o nome do usuário e exibe uma mensagem personalizada, incluindo a hora atual.
📌 Passos:
Solicitar o nome do usuário com input().
Utilizar a biblioteca datetime para obter a hora atual.
Exibir uma mensagem personalizada com o nome e a hora atual.

Checklist de Entrega
✅ Programa que exibe uma mensagem personalizada.
✅ Uso de input() para capturar o nome do usuário.
✅ Uso da biblioteca datetime para exibir a hora atual.
✅ Código enviado para o repositório GitHub na pasta Modulo_01/.

