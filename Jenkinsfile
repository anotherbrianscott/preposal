pipeline {
      environment {
    image = "awareness"
    ecr = "350919162912.dkr.ecr.us-west-2.amazonaws.com/awareness"
    ecrCred = 'ecr'
    dockerImage = ''
  }
    agent { dockerfile true }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
            }
        }
    stage('Deploy Master Image') {
    when {
      anyOf {
            branch 'master'
      }
     }
      steps{
        script {
          docker.withRegistry(ecr, ecrcred) {     
            dockerImage.push("$BUILD_NUMBER")
             dockerImage.push('latest')

          }
        }
      }
     }    
    }
}
