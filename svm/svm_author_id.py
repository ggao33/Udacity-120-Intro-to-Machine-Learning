#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
features_train = features_train[:int(len(features_train)//100)]
labels_train = labels_train[:int(len(labels_train)//100)]

#########################################################
### your code goes here ###
from sklearn import svm
linear_clf = svm.SVC(kernel = "linear")
linear_clf.fit(features_train,labels_train)
pred = linear_clf.predict(features_test)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(pred,labels_test))
print(confusion_matrix(pred,labels_test))
#########################################################
from sklearn import svm
rbf_clf = svm.SVC(kernel = "rbf",C = 10000)
rbf_clf.fit(features_train,labels_train)
pred = rbf_clf.predict(features_test)

from sklearn.metrics import classification_report,confusion_matrix
print(classification_report(pred,labels_test))
print(confusion_matrix(pred,labels_test))
print("The answer is: ")
print(pred[10])
print(pred[26])
print(pred[50])
print("How many are predicted to be in Chris 1 class")
print(sum(pred == 1))
