# Utiliza uma imagem oficial do Python
FROM python:3.13-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o programa para a imagem
COPY app.py financeiro.py ./

# Executa o programa quando o container iniciar
CMD ["python", "app.py"]