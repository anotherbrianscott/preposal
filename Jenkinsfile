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
          sh "docker build --build-arg APP_NAME=receipts -t 350919162912.dkr.ecr.us-west-2.amazonaws.com/awareness:latest -f docker/prod/Dockerfile ."
        }
      }
    }
  }
} 
