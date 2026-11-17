pipeline {
    agent {
        docker { image 'python:3.10-bullseye' }
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/zhrv80-prog/Portfolio_project_tests.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh '''
                  python -m pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                withCredentials([string(credentialsId: 'my-app-password', variable: 'MY_APP_PASSWORD')]) {
                    sh 'pytest tests/ --junitxml=results/test-results.xml'
                    sh 'ls -la results/'
                    stash includes: 'results/test-results.xml', name: 'test-results'
                }
            }
        }
    }
    post {
        always {
            node('Jenkins') {
                unstash 'test-results'
                junit 'results/test-results.xml'
            }
        }
    }
}