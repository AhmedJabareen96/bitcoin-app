pipeline {
    agent {label 'worker-0'}
    stages{
    stage("Clone"){
        steps{
        git branch: 'main', url: 'https://github.com/AhmedJabareen96/bitcoin-app.git'
        }
    }
    stage("Build Docker"){
        steps{
        sh 'docker build -t bitcoin-rate-app:$BUILD_NUMBER .'
    }
    }
    stage('Tag Docker') {
steps {
sh 'docker tag bitcoin-rate-app:$BUILD_NUMBER ahmedjabareen/bitcoin-rate-app:$BUILD_NUMBER'
}
}
stage('Push Docker') {
steps {
withCredentials([usernamePassword(credentialsId: 'dockerhub', passwordVariable: 'pass', usernameVariable: 'username')]) {
// the code here can access $pass and $user
sh 'docker login -u ${username} -p ${pass}'
sh 'docker push ahmedjabareen/bitcoin-rate-app:$BUILD_NUMBER'
}
}
}
}
}