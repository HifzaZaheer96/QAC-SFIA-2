pipeline {
    agent any
    stages {
        stage('Development Environment') {
            steps {
                sh 'chmod +x ./script/*'
                sh './script/before_installation.sh'
                sh './script/installation.sh'
                sh './script/ansible.sh'
                sh './script/docker.sh'
                
                
            }
        }
        stage('Wait for installation'){
            steps{
                
                sh 'sleep 20'
               
            }
        }

         stage('Testing'){
            steps {
                sh './script/testing.sh'

            }
         }
    }
}
