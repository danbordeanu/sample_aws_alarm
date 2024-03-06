pipeline {

    agent { label "shared-agent" }

    // options
    options {
        durabilityHint('PERFORMANCE_OPTIMIZED')
        ansiColor('xterm')
        timestamps()
        buildDiscarder logRotator(artifactDaysToKeepStr: '14', artifactNumToKeepStr: '', daysToKeepStr: '14', numToKeepStr: '')
        skipStagesAfterUnstable()
        parallelsAlwaysFailFast()
        disableConcurrentBuilds()
    }

    // set env for conda
    environment {
    PATH = "${tool 'Conda'}:${env.WORKSPACE}/.condaenv/bin:${PATH}"
    CONDA_ENV_PATH = "${env.WORKSPACE}/.condaenv"
    }

    stages {

            stage('Prepare testing environment') {
                steps {
                    sh '''./env_setup.sh'''
                    }
            }

            // run pylint and flake8 tests
            // stage('Python tests') {
            // parallel {
               // stage('pylint') {
                 //   steps {
                   //     sh '''pylint **/**/*.py -f parseable > report.pylint.txt'''
                    // }
                // }
                // stage('flake8') {
                   // steps {
                     //   sh '''flake8 --format=pylint --tee --output-file=report.flake8.txt **/**/*.py'''
                       // }
                    // }
                // }
            // }

            stage('Build package') {
                when {
                    expression {
                        currentBuild.result == null || currentBuild.result == 'SUCCESS'
                    }
                }

                // build package
                steps {
                    sh  '''python3 setup.py sdist bdist_wheel
                        '''
                }
                post {
                    always {
                        // Archive unit tests for the future
                        archiveArtifacts (allowEmptyArchive: true,
                                     artifacts: 'dist/*whl',
                                     fingerprint: true)
                    }
                }
            }
            // create pypirc file in prj root
            stage('Create pypirc file') {
                steps{
                    // get credentials from stored credentials
                    withCredentials([[$class:'UsernamePasswordMultiBinding', credentialsId:'PIP_CREDENTIALS', usernameVariable:'PIP_USER', passwordVariable:'PIP_PASS']]) {
                    sh '''cat <<EOF > .pypirc
                    [distutils]
                    index-servers = local
                    [local]
                    repository: https://artifacts.host.com/artifactory/api/pypi/pypi-host-dev
                    username: $PIP_USER
                    password: $PIP_PASS
                    '''
                    }
                }
            }
            // publish package to artifactory
            stage('Publish package') {
                steps {
                 sh '''python3 setup.py sdist upload -r local
                    '''
                }
            }
    }

     post {
        // we want to keep test results for 14 days at least (see above)
        always {
            archiveArtifacts(artifacts: 'report.*.txt', allowEmptyArchive: true, fingerprint: true, onlyIfSuccessful: false)
        }
         failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
                to: 'dan.bordeanu@host.com'
            )
        }
        success {
              emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                         <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
                to: 'dan.bordeanu@host.com'
            )
         }

        // cleanup
        cleanup {
            deleteDir()
        }
    }
}

