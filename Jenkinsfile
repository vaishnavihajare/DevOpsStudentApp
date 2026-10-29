pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Python Application') {
            steps {
                bat 'python hello.py'
            }
        }

        stage('Run Pytest') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t devopsstudentapp:uat .'
            }
        }

        stage('Evidently Check') {
            steps {
                bat 'python -c "import evidently; print(\'Evidently installed successfully\')"'
            }
        }
    }
}