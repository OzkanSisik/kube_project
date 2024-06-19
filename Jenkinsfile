pipeline {
    agent any

    stages {

        stage('Install dependencies') {
            steps {
                // Install Python and dependencies (pytest and selenium) using pip
                sh 'python3 -m pip install --upgrade pip'
                sh 'python3 -m pip install pytest selenium'
            }
        }

        stage('Run tests') {
            steps {
                // Run pytest command to execute your tests
                sh 'pytest test_ozkan.py'  // Replace with your actual test file/module name
            }

        }
    }

    // Additional post-build actions can be added here if needed
    // For example, sending notifications, publishing reports, etc.
}
