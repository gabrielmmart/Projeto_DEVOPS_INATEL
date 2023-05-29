pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Instalar dependencias') {
            steps {
                script {
                    sh 'python -m pip install -U pip'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Unit Testing') { // Perform unit testing
            steps {
             script {
                    sh """
                    python -m unittest discover -s tests/unit
                    """
                }
            }
        }

        stage ('Notifications'){
            steps {
                echo 'Notifications'
                sh '''
                    cd scripts/
                    chmod 777 *
                    ./jenkins.sh
                   '''
            }

        }
    }
}