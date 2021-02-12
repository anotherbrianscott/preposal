pipeline {
    agent { dockerfile true }
    stages {
        stage ('Checkout') {
            steps {
               git 'https://github.com/anotherbrianscott/preposal.git' 
            }
          }
       }
    {
        stage ('Docker push') {
            steps {
        docker.withRegistry('https://350919162912.dkr.ecr.us-west-2.amazonaws.com') {
        docker.image('demo').push('latest')
                  }
              }
        }
    }        
}
