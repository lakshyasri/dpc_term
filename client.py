import boto3
import paramiko
import psutil
import awscli
import aws

cpu_use = psutil.cpu_percent(interval=1, percpu=False)
print(cpu_use)

if cpu_use < 50:

    ec2 = boto3.resource('ec2')

    instances = ec2.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    for instance in instances:
        print(instance.id, instance.instance_type)
    x = int(input("Enter 1 for monte carlo: \n 2 for Stcok prediction"))
    if x == 1:
        try:
            name = str(input("Enter your name"))
            #stock = str(input("Enter Stock Symbol"))
            samples = (input("Enter Number of samples to be created"))
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            privkey = paramiko.RSAKey.from_private_key_file('C:/Users/Laksh/Desktop/ec2_dpc.pem')
            ssh.connect(instance.public_dns_name, username='ec2-user', pkey=privkey)
            stdin, stdout, stderr = ssh.exec_command('python create.py m' + str(name) + " " + str(samples))
            ssh.close()
        except:
            print("Error while executing the shell command on the instance")
    if x == 2:
        try:
            name = str(input("Enter your name"))
            samples = str(input("Enter Stock Symbol"))
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            privkey = paramiko.RSAKey.from_private_key_file('C:/Users/Laksh/Desktop/ec2_dpc.pem')
            ssh.connect(instance.public_dns_name, username='ec2-user', pkey=privkey)
            stdin, stdout, stderr = ssh.exec_command('python create1.py s' + str(name) + " " + str(samples))
            ssh.close()
        except:
            print("Error while executing the shell command on the instance")

    # final = (int(x) / int(i))
    # print('final number of samples per slave:', final)
else:
    print("high cpu usage try again")
