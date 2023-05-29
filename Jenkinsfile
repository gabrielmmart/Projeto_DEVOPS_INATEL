pipeline {
  options {
    buildDiscarder(logRotator(numToKeepStr: '10')) // Retain history on the last 10 builds
    ansiColor('xterm') // Enable colors in terminal
    timestamps() // Append timestamps to each line
    timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
  }
  agent {
    dockerfile { filename 'Dockerfile.build' }
  }
  stages {  
    stage('Checkout') {
      steps {
        checkout scm
      }
    }
    stage('Instalar dependencias') {
      steps {
        script {
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