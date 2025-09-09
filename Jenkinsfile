pipeline {
    agent any

    stages {
        stage('Check Python') {
            steps {
                bat 'python --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install selenium pandas'
            }
        }

        stage('Run Python Files') {
            steps {
                bat 'python Instance_Static_methods.py'
                bat 'python Local_Global_Variables.py'
            }
        }
    }
}
