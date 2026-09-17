pipeline {
    agent any

    stages {
        stage('Code Integration') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/dhanujashree/shopeasy.git'
            }
        }

        stage('Build') {
            steps {
                bat 'if exist index.html (echo Build successful) else (echo index.html not found & exit /b 1)'
            }
        }

        stage('Automated Testing') {
            steps {
                bat '"C:\\Program Files\\Python313\\python.exe" test_shopeasy.py'
            }
        }

        stage('Report Generation') {
            steps {
                bat 'echo Automated Selenium test report generated'
            }
        }

        stage('Deployment') {
            steps {
                bat 'if not exist deploy mkdir deploy'
                bat 'copy /Y index.html deploy\\index.html'
                bat 'echo Deployment completed successfully'
            }
        }
    }
}
