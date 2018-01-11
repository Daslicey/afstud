import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import csv

with open('lasdatatrain.csv', newline='') as csvfile:
    trainData = csv.reader(csvfile, delimiter=';')
    next(trainData)
    for row in trainData:
        x = [row[12:15], 1]
        y = [row[16:19], 1]


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3,random_state= 1)

clf_gini = DecisionTreeClassifier(criterion= "gini", random_state= 100,
                                  max_depth=3, min_samples_leaf=5)
clf_gini.fit(x_train, y_train)
#with open('lasdatatarget.csv', newline='') as csvfile:
 #   targetData = csv.reader(csvfile, delimiter=';')
  #  next(targetData)
   # for row in targetData:
    #    print (row[1:4], row[12:19])