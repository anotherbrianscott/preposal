pipeline {
  environment {
    image = "awareness"
    ecr = "350919162912.dkr.ecr.us-west-2.amazonaws.com/awareness"
    ecrCredential = 'ecr'
    dockerImage = ''
  }
  agent { dockerfile true }
  stages {
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build ecr + ":$BUILD_NUMBER"
        }
      }
    }
  }
} 
