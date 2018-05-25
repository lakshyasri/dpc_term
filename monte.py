# from first import x
# from first import name
import quandl
import pandas as pd
import numpy as np
import datetime
import scipy
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation, svm
from threading import Thread
from time import sleep
from first import instance
from random import random
import boto3
import paramiko
import psutil

cpu_use = psutil.cpu_percent(interval=1, percpu=False)
print(cpu_use)
ec2 = boto3.resource('ec2')

y = 5
while y != 0:
    print("1. Press 1 to connect \n2. Press 2 to get Monte Carlo job \n3. Press 3 for Stock prediction job \n4. Press "
          "4. to disconnect")
    y = int(input("Enter your choice: "))
    if y == 1:
        instances = ec2.create_instances(
            ImageId='ami-976152f2',
            MinCount=1,
            MaxCount=1,
            KeyName="ec2_dpc",
            InstanceType="t2.micro"
        )
    condition = True
    if y == 2:
        while condition:
            try:

                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                privkey = paramiko.RSAKey.from_private_key_file('C:/Users/Laksh/Desktop/ec2_dpc.pem')
                ssh.connect(instance.public_dns_name, username='ec2-user', pkey=privkey)
                stdin, stdout, stderr = ssh.exec_command('python m*.py')
                stdin.flush()
                data = stdout.read().splitlines()
                for line in data:
                    input_user = line.decode()
                    print(input_user)
                stdin, stdout, stderr = ssh.exec_command('ls m*.py')
                stdin.flush()
                data = stdout.read().splitlines()
                for line in data:
                    name = line.decode()
                count = 0
                stdin, stdout, stderr = ssh.exec_command('rm m*.py')
                for line in data:
                    count += 1

                if count != 0:
                    try:

                        def main():
                            n = getInput()
                            pi = simulate(n)
                            printResults(pi, n)
                            client = str(name)
                            print("result for client", client)
                            ssh = paramiko.SSHClient()
                            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                            privkey = paramiko.RSAKey.from_private_key_file('C:/Users/Laksh/Desktop/ec2_dpc.pem')
                            ssh.connect(instance.public_dns_name, username='ec2-user', pkey=privkey)
                            ssh.exec_command('python result.py ' + str(client) + " " + str(client) + " " + str(pi))
                            ssh.close()


                        def getInput():
                            n = int(input_user)
                            return n


                        def simulate(n):
                            hit = 0
                            for i in range(n):
                                result = simulateOne()
                                if result == 1:
                                    hit = hit + 1
                                pi = 4 * float(hit) / n
                            return pi


                        def simulateOne():
                            x = genCoord()
                            y = genCoord()
                            distance = x * x + y * y
                            if distance <= 1:
                                return 1
                            else:
                                return 0


                        def genCoord():
                            oord = 2 * random() - 1
                            return oord


                        def printResults(pi, n):
                            print("number of simulations running :", n)
                            print("Estimated value of pi : ", pi)


                        if __name__ == "__main__": main()
                    except:
                        print("Result printed")
            except KeyboardInterrupt:
                print("interrupted")

    if y == 3:
        while condition:
            try:
                input_symbol = ""
                name = ""
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                privkey = paramiko.RSAKey.from_private_key_file('C:/Users/Laksh/Desktop/ec2_dpc.pem')
                ssh.connect(instance.public_dns_name, username='ec2-user', pkey=privkey)
                stdin, stdout, stderr = ssh.exec_command('python s*.py')
                stdin.flush()
                data = stdout.read().splitlines()
                for line in data:
                    input_symbol = line.decode()
                #print(input_symbol)
                #print(('("WIKI/' + str(input_symbol) + '")'))
                stdin, stdout, stderr = ssh.exec_command('ls s*.py')
                stdin.flush()
                data = stdout.read().splitlines()
                count = 0
                for line in data:
                    name = line.decode()
                    count += 1
                #print(('("WIKI/' + str(input_symbol)+ '")'))
                #print("(WIKI/"+input_symbol+")")
                stdin, stdout, stderr = ssh.exec_command('rm s*.py')
                if count != 0:

                        symbol = str(input_symbol)
                        # print('WIKI/' + str(input_symbol) + '")')

                        df = quandl.get('WIKI/' + str(symbol))


                        #print(df.tail())

                        df = df[['Adj. Close']]
                        forecast_out = int(30)  # predicting 30 days into future
                        df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)  # label column with data shifted 30 units up
                        # print(df.tail())
                        X = np.array(df.drop(['Prediction'], 1))
                        X = preprocessing.scale(X)
                        X_forecast = X[-forecast_out:]  # set X_forecast equal to last 30
                        X = X[:-forecast_out]  # remove last 30 from X
                        y = np.array(df['Prediction'])
                        y = y[:-forecast_out]
                        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.2)
                        # Training
                        clf = LinearRegression()
                        clf.fit(X_train, y_train)
                        # Testing
                        confidence = clf.score(X_test, y_test)
                        print("confidence: ", confidence)
                        forecast_prediction = clf.predict(X_forecast)
                        print(forecast_prediction)
                        ssh = paramiko.SSHClient()
                        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        privkey = paramiko.RSAKey.from_private_key_file('C:/Users/Laksh/Desktop/ec2_dpc.pem')
                        ssh.connect(instance.public_dns_name, username='ec2-user', pkey=privkey)
                        ssh.exec_command('python result.py ' + str(name) + " " + str(name) + " " + str(forecast_prediction))
                        ssh.close()

            except KeyboardInterrupt:
               print("interrupted")
else:
    print("bye")
