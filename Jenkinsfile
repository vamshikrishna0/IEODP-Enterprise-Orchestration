pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/vamshikrishna0/IEODP-Enterprise-Orchestration.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh 'sonar-scanner'
                }
            }
        }


        stage('Check Docker') {
            steps {
                sh 'docker --version'
                sh 'docker-compose --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ieodp .'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }

    }
}
