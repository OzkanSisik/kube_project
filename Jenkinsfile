pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                pip install pytest
            }
        }
        stage('Test') {
            steps {
                sh 'python3 test_ozkan.py'
            }
        }
    }
}