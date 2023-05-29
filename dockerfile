# Define nossa imagem base
FROM jenkins/jenkins:lts-jdk11

# Define nosso usuario dentro do container
USER root

# Executa comandos para instalar o pip
RUN apt-get update
RUN apt-get install -y python-pip
RUN pip install --upgrade pip

# Define uma variavel de ambiente MAVEN_HOME que aponta para o local do maven
ENV MAVEN_HOME /opt/maven

# chown: comando linux que muda o dono de uma pasta. Nesse caso estamos dando permissao para o usuario jenkins
RUN chown -R jenkins:jenkins /opt/maven

# Instalando mailutils
RUN apt-get install -y mailutils

# Limpa arquivos baixados com apt-get
RUN apt-get clean

USER jenkins