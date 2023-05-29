pipeline {
    agent any
    
    environment {
        NOTIF_EMAIL = 'gabriel.medeiros@ges.inatel.br'
    }
    
    stages {
        stage('Instalar dependencias') {
            steps {
                script {
                    sh 'python3 -m pip install -U pip'
                    sh 'pip install -r requirements.txt'
                }

            }
        }
        stage('Unit Testing') { // Perform unit testing
            steps {
             script {
                    sh """
                    python3 -m unittest discover -s /
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
