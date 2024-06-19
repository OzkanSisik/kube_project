pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.8.12'  // Specify the Python version you want to install
    }

    stages {
        stage('Install Python') {
            steps {
                // Install Python 3 from python.org on macOS
                script {
                    def pythonDownloadUrl = "https://www.python.org/ftp/python/${env.PYTHON_VERSION}/python-${env.PYTHON_VERSION}-macosx10.9.pkg"
                    sh "curl -O ${pythonDownloadUrl}"
                    sh "sudo installer -pkg python-${env.PYTHON_VERSION}-macosx10.9.pkg -target /"
                    sh "python${env.PYTHON_VERSION} -m ensurepip"
                    sh "python${env.PYTHON_VERSION} -m pip install --upgrade pip setuptools wheel"
                }
                // Verify Python and pip installation
                sh "python${env.PYTHON_VERSION} --version"
                sh "pip${env.PYTHON_VERSION} --version"
            }
        }

        stage('Install dependencies') {
            steps {
                // Install pytest and selenium using pip
                sh "pip${env.PYTHON_VERSION} install --upgrade pip"
                sh "pip${env.PYTHON_VERSION} install pytest selenium"
            }
        }

        stage('Run tests') {
            steps {
                // Run pytest command to execute your tests
                sh "python3 test_ozkan.py"  // Replace with your actual test file/module name
            }


        }
    }

    // Additional post-build actions can be added here if needed
    // For example, sending notifications, publishing reports, etc.
}
