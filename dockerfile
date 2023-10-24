# Use a imagem oficial do Python como imagem base
FROM python:3.8-slim

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY requirements.txt requirements.txt

# Instale as dependências
RUN pip install -r requirements.txt

# Copie o restante do código para o diretório de trabalho
COPY . .

# Exponha a porta 5000 para que o Flask possa ouvir as solicitações
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
