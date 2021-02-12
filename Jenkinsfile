pipeline {
    agent {
        docker { image 'python:3.7' }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    }
}
