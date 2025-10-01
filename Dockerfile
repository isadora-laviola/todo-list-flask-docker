# PASSO 1: A IMAGEM DE BASE
# Dizemos ao Docker para começar com uma imagem oficial que já tem o Python 3.11.
# A versão "-slim" é mais leve, o que é ótimo.
FROM python:3.11-slim

# PASSO 2: O DIRETÓRIO DE TRABALHO
# Criamos uma pasta chamada /app dentro do contêiner para organizar nosso projeto.
WORKDIR /app

# PASSO 3: COPIAR E INSTALAR AS DEPENDÊNCIAS
# Copiamos o arquivo de requisitos PRIMEIRO para aproveitar o cache do Docker.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# PASSO 4: COPIAR O CÓDIGO DA APLICAÇÃO
# Agora copiamos o resto dos arquivos do nosso projeto (o app.py) para dentro do contêiner.
COPY . .

# PASSO 5: O COMANDO DE EXECUÇÃO
# Definimos o comando que será executado quando o contêiner iniciar.
# Isso é o equivalente a rodar "python app.py" no nosso terminal.
CMD ["python", "app.py"]