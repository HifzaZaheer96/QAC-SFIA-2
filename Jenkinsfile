pipeline {
    agent any
    stages {
        stage('Development Environment') {
            steps {
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh './script/make_service.sh'
                sh './script/ansible.sh'
            }
        }
        stage('Wait for installation'){
            steps{
                
                sh 'sleep 60'
               
            }
        }

         stage('Testing'){
            steps {
                sh './script/testing.sh'

            }
         }
    }
}

