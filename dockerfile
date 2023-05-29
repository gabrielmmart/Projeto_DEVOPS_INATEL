# Base image
FROM jenkins/jenkins:lts

# Switch to the root user
USER root

# Install Python and pip
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Install required Python packages
RUN pip3 install jenkins

# Switch back to the Jenkins user
USER jenkins
