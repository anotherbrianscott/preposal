pipeline {
    agent { dockerfile true }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'python test.py'
      }
        
    stage('deploy') {
  steps {
    echo 'deploying image to environment'
  }
}
      post {
        always {
          junit 'test-reports/*.xml'
        }
      }    
    }
  }
}
