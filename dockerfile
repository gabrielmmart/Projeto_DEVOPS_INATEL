# Base image
FROM jenkins/jenkins:lts-jdk11

# Switch to the root user
USER root

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Install any additional dependencies you may need
# RUN apt-get install -y <your-package-name>

# Install Python packages using pip
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt


# Instalando mailutils
RUN apt-get update && apt-get install -y mailutils

USER jenkins

EXPOSE 8080
