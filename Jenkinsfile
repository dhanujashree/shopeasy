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
                bat '"C:\\Program Files\\Python313\\python.exe" -m pip install -r requirements.txt'
                bat '"C:\\Program Files\\Python313\\python.exe" test_shopeasy.py'
            }
        }

        stage('Report Generation') {
            steps {
                bat 'if exist test-report.html (echo Test report generated successfully) else (echo Test report not found & exit /b 1)'
                archiveArtifacts artifacts: 'test-report.html', fingerprint: true
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
