pipeline {
  environment {
    registry = "350919162912.dkr.ecr.us-west-2.amazonaws.com/awareness"
    registryCredential = 'dockerhub'
    dockerImage = ''
  }
  agent { dockerfile true }
  stages {
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build awareness
        //  dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
  //  stage('Deploy Image') {
   //   steps{
     //   script {
   //       docker.withRegistry( '', registryCredential ) {
   //         dockerImage.push()
   //       }
 //       }
  //    }
//    }
 //   stage('Remove Unused docker image') {
 //     steps{
  //      sh "docker rmi $registry:$BUILD_NUMBER"
  //    }
  //  }
  }
}
