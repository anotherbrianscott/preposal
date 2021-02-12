pipeline {
    agent { dockerfile true }
    stages {
        stage ('Checkout')
        git 'https://github.com/anotherbrianscott/preposal.git' 
    }
    {
        stage ('Docker push')
        docker.withRegistry('https://350919162912.dkr.ecr.us-west-2.amazonaws.com', 'AKIAVDNDJPQQP3QFCZ6P:AWSServiceRoleForECRReplication') {
        docker.image('demo').push('latest')
  }
 }
}
