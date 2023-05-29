# Define nossa imagem base
FROM jenkins/jenkins:lts-jdk11

# Define nosso usuario dentro do container
USER root

FROM python:3

WORKDIR /

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./supermercadoMain.py" ]
# Instalando mailutils
RUN apt-get install -y mailutils

# Limpa arquivos baixados com apt-get
RUN apt-get clean

USER jenkins