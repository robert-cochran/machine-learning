#import numpy as np
import logging
import csv
#from numpy import genfromtxt
#import pandas as pd
from sklearn import datasets
import random

#to do
#1. print the generated model
#2. print the error of the model
#3. print a graph showing the model against the data


X, y = datasets.load_boston(return_X_y=True)


housingPrice = y
avgRooms = X[:,4]

theta = random.random()
beta = random.random()

model = [theta, beta]


 
