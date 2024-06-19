pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8.12'  // Specify the Python version you want to install
    }

    stages {
        stage('Install Python') {
            steps {
                // Install Python 3 using apt-get (Linux) or choco (Windows)
                script {
                    script {
                    sh 'brew install python@3.8'
                    sh 'python3 -m ensurepip'
                    sh 'python3 -m pip install --upgrade pip setuptools wheel'
                }
                // Verify Python and pip installation
                sh 'python3 --version'
                sh 'pip3 --version'
            }
        }

        stage('Install dependencies') {
            steps {
                // Install pytest and selenium using pip
                sh 'pip3 install --upgrade pip'
                sh 'pip3 install pytest selenium'
            }
        }

        stage('Run tests') {
            steps {
                // Run pytest command to execute your tests
                sh 'python3 test_ozkan.py'  // Replace with your actual test file/module name
            }

            post {
                // Archive the test results for later reference
                always {

