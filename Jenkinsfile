pipeline {
    agent 
    { label docker { dockerfile true } }
    stages {
        stage('build') {
            steps {
                sh 'docker build -t awareness .'
            }
        }
    }
       post {
        always {
            junit 'build/reports/**/*.xml'
        }
    } 
}
