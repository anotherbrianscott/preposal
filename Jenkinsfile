pipeline {
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'python test.py'
            }
        }
    }
}
