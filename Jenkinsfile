pipeline {
  environment {
    image = "awareness"
    ecr = "350919162912.dkr.ecr.us-west-2.amazonaws.com/awareness"
    ecrCred = 'ecr'
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
  stage('Deploy Master Image') {
    when {
      anyOf {
            branch 'master'
      }
     }
      steps{
        script {
          docker.withRegistry(ecrurl, ecrcred) {     
            dockerImage.push("$BUILD_NUMBER")
             dockerImage.push('latest')

          }
        }
      }
    }

    stage('Remove Unused docker image - Master') {
      when {
      anyOf {
            branch 'master'
     }
}
