pipeline {
  // Assign to docker slave(s) label, could also be 'any'
  agent {
    label 'docker' 
  }

  stages {
    stage('Docker python test') {
      agent {
        docker {
          // Set both label and image
          label 'docker'
          image 'python:3.7'
          args '--name docker-python' // list any args
        }
      }
      steps {
        // Steps run in python:3.7 docker container on docker slave
        sh 'python --version'
      }
    }

    stage('Docker maven test') {
      agent {
        docker {
          // Set both label and image
          label 'docker'
          image 'maven:3-alpine'
        }
      }
      steps {
        // Steps run in maven:3-alpine docker container on docker slave
        sh 'mvn --version'
      }
    }
  }
} 
