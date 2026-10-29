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
                bat '"C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" --version'
            }
        }

        stage('Create Python Environment') {
            steps {
                bat '"C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m venv .venv-ci'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.venv-ci\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Python Application') {
            steps {
                bat '.venv-ci\\Scripts\\python.exe hello.py'
            }
        }

        stage('Run Pytest') {
            steps {
                bat '.venv-ci\\Scripts\\python.exe -m pytest -v'
            }
        }

        stage('Docker Build') {
    steps {
        bat '"C:\\Users\\Admin\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t devopsstudentapp:uat .'
    }
}

        stage('Evidently Check') {
            steps {
                bat '.venv-ci\\Scripts\\python.exe -c "import evidently; print(\'Evidently installed successfully\')"'
            }
        }
    }
}