#!usr/bin/python

import random

def prepData(points = 1000):
    random.seed(42)
    grade = [random.random() for i in range(0, points)]
    bumpy = [random.random() for i in range(0, points)]
    error = [random.random() for i in range(0, points)]
    y = [round(grade[i]*bumpy[i]+0.9+0.1*error[i]) for i in range(0, points)]
    for i in range(0, len(y)):
        if grade[i] > 0.8 or bumpy[i] > 0.8:
            y[i]=1.0
            
    X = [[g,s] for g,s in zip(grade, bumpy)]
    print (X)