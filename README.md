# Projeto de Introdução ao Python

Este projeto é uma coleção de exemplos e atividades práticas para introduzir os conceitos básicos da linguagem Python. Ele inclui desde o primeiro programa em Python até um projeto prático que interage com o usuário e exibe a hora atual.

---

## 🚀 Como Usar

### Pré-requisitos
- **Python 3.x** instalado no seu computador.
- Um editor de texto ou IDE (recomendamos [VS Code](https://code.visualstudio.com/) ou [PyCharm](https://www.jetbrains.com/pycharm/)).

### Configuração do Ambiente
1. **Instale o Python**:
   - Baixe e instale o Python a partir do [site oficial](https://www.python.org/).
   - Verifique a instalação executando no terminal:
     ```bash
     python --version
     ```
     ou
     ```bash
     python3 --version
     ```

2. **Clone o repositório**:
   - Se você estiver usando Git, clone este repositório:
     ```bash
     git clone https://github.com/seu-usuario/nome-do-repositorio.git
     ```

3. **Navegue até a pasta do projeto**:
   - No terminal, acesse a pasta onde os arquivos estão salvos:
     ```bash
     cd nome-do-repositorio
     ```

---

## 📂 Estrutura do Projeto

O projeto contém os seguintes arquivos:

1. **`primeiro_programa.py`**:
   - Um programa simples que exibe "Olá, mundo!" no terminal.

2. **`variaveis_tipos.py`**:
   - Exemplo de uso de variáveis e tipos de dados em Python.

3. **`manipulacao_strings.py`**:
   - Demonstração de métodos para manipulação de strings, como `strip()` e `lower()`.

4. **`input_usuario.py`**:
   - Um programa que solicita o nome do usuário e exibe uma mensagem personalizada.

5. **`desafio_hora_atual.py`**:
   - Um desafio que exibe a hora atual junto com uma saudação personalizada.

6. **`programa_personalizado.py`**:
   - Um projeto prático que combina entrada do usuário e exibição da hora atual.

---

## ▶️ Como Executar os Códigos

Para executar qualquer um dos arquivos Python, siga os passos abaixo:

1. Abra o terminal na pasta do projeto.
2. Execute o arquivo desejado com o comando:
   ```bash
   python nome_do_arquivo.py
   ```
   ou
   ```bash
   python3 nome_do_arquivo.py
   ```

Exemplo:
```bash
python primeiro_programa.py
```

---

## 🧠 O Que Você Vai Aprender

- **Sintaxe básica do Python**: Como escrever e executar programas simples.
- **Variáveis e tipos de dados**: Como armazenar e manipular informações.
- **Manipulação de strings**: Como trabalhar com textos em Python.
- **Interação com o usuário**: Como usar a função `input()` para capturar dados.
- **Trabalhando com datas e horas**: Como usar a biblioteca `datetime` para exibir a hora atual.

---

## 📝 Exemplos de Códigos

### 1. Primeiro Programa (`primeiro_programa.py`)
```python
print("Olá, mundo!")
```

### 2. Variáveis e Tipos de Dados (`variaveis_tipos.py`)
```python
nome = "Maria"
idade = 25
altura = 1.68
estudante = True

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura}, Estudante: {estudante}")
```

### 3. Manipulação de Strings (`manipulacao_strings.py`)
```python
mensagem = "  Python é divertido!  "
print(mensagem.strip())  # Remove espaços em branco
print(mensagem.lower())  # Converte para minúsculas
```

### 4. Interação com o Usuário (`input_usuario.py`)
```python
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}! Bem-vindo ao curso de Python.")
```

### 5. Desafio: Hora Atual (`desafio_hora_atual.py`)
```python
from datetime import datetime

nome = input("Qual é o seu nome? ")
agora = datetime.now()
hora_atual = agora.strftime("%H:%M")
print(f"Olá, {nome}! Agora são {hora_atual}.")
```

### 6. Projeto Prático (`programa_personalizado.py`)
```python
from datetime import datetime

nome = input("Qual é o seu nome? ")
agora = datetime.now()
hora_atual = agora.strftime("%H:%M")
print(f"Olá, {nome}! Agora são {hora_atual}.")
```

---

## 📌 Dicas Extras

- **Explore outros métodos de strings**: Experimente métodos como `replace()`, `split()`, `upper()`, etc.
- **Adicione funcionalidades**: Tente modificar o programa para exibir a data completa ou adicionar mais interações com o usuário.
- **Pratique**: Crie seus próprios programas usando os conceitos aprendidos.

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🤝 Contribuições

Contribuições são bem-vindas! Se você tiver sugestões ou melhorias, sinta-se à vontade para abrir uma **issue** ou enviar um **pull request**.

---

Espero que esse README seja útil! Se precisar de mais ajustes ou informações, é só avisar. 😊
