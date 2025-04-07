pipeline {
    agent any

    environment {
        PYTHONPATH = "${WORKSPACE}"
    }

    stages {
        stage('Setup') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    xvfb-run -a pytest tests/ --alluredir=allure_results
                '''
            }
        }

        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'allure_results']]
            }
        }
    }
}
