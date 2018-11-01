from dataPrep import prepData
from visualize import plotIt
from gaussian_nb_classify import classify

import numpy as np
import pylab as pl

features_train, labels_train, features_test, labels_test = prepData()

grade_fast = [features_train[i][0] for i in range(0, len(features_train)) if labels_train[i]==0]
bumpy_fast = [features_train[i][1] for i in range(0, len(features_train)) if labels_train[i]==0]
grade_slow = [features_train[i][0] for i in range(0, len(features_train)) if labels_train[i]==1]
bumpy_slow = [features_train[i][0] for i in range(0, len(features_train)) if labels_train[i]==1]

clf = classify(features_train, labels_train)

plotIt(clf, features_test, labels_test)

output_image("test.png","png",open("test.png","rb").read())