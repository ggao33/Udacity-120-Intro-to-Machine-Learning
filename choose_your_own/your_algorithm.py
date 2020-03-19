#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
from time import time
#KNN
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors = 3)
t0 = time()
clf.fit(features_train, labels_train)
print("KNN training time is: " + str(round(time()-t0,3)) + "s")
t1 = time()
pred = clf.predict(features_test)
print("KNN predicting time is: " + str(round(time()-t1,3)) + "s")

from sklearn.metrics import classification_report,confusion_matrix
print("KNN results:")
print(classification_report(pred,labels_test))
print(confusion_matrix(pred,labels_test))
# n = 3 accuracy = 0.94
# n = 5 accuracy = 0.92

#adaboost
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(n_estimators = 100, random_state = 0)
t2 = time()
clf.fit(features_train, labels_train)
print("Adaboost training time is: " + str(round(time()-t2,3)) + "s")
t3 = time()
pred = clf.predict(features_test)
print("Adaboost predicting time is: " + str(round(time()-t3,3)) + "s")

from sklearn.metrics import classification_report,confusion_matrix
print("Adaboost results:")
print(classification_report(pred,labels_test))
print(confusion_matrix(pred,labels_test))
# accuracy = 0.92

#random forest
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(max_depth = 2,random_state = 0)
t4 = time()
clf.fit(features_train, labels_train)
print("Random Forest training time is: " + str(round(time()-t4,3)) + "s")
t5 = time()
pred = clf.predict(features_test)
print("Random Forest predicting time is: " + str(round(time()-t5,3)) + "s")

from sklearn.metrics import classification_report,confusion_matrix
print("Random Forest results:")
print(classification_report(pred,labels_test))
print(confusion_matrix(pred,labels_test))
#accuracy= 0.92


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
