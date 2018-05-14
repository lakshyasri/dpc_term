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
   