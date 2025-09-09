pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/Amymah/gitjenkinsintegration.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // If you have requirements.txt in repo
                //bat 'pip install -r requirements.txt'

                // Or install specific packages directly (example: selenium, pandas)
                bat 'pip install selenium pandas'
            }
        }

        stage('Run Python Files') {
            steps {
                bat 'python Class_and_Objects.py'
                bat 'python Class_and_Objects_example.py'
            }
        }
    }
}
