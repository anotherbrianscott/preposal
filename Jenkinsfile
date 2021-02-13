pipeline {
    agent { dockerfile true }
    stages {
        stage('build') {
            steps {
                docker build -t "learinngapi"
            }
        }
    }
}
