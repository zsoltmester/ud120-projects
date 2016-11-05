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
from sklearn.metrics import accuracy_score

def execute(clf, output_name):
    t0 = time()
    clf.fit(features_train, labels_train)
    print "training time:", round(time()-t0, 3), "s"

    t0 = time()
    pred = clf.predict(features_test)
    print "prediction time:", round(time()-t0, 3), "s"
    print "accuracy: ", accuracy_score(pred, labels_test)

    prettyPicture(clf, features_test, labels_test, output_name)

### Naive Bayes
print "--- Naive Bayes ---"
from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()
execute(clf, "naive_bayes")

### SVM
print "--- SVM ---"
from sklearn import svm
clf = svm.SVC(kernel="rbf", C=10000)
execute(clf, "svm")

## Decision Tree
print "--- Decision Tree ---"
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=40)
execute(clf, "decision_tree")

## K Nearest Neighbors
print "--- K Nearest Neighbors ---"
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=1)
execute(clf, "k_nearest")

## Radius Neighbors
print "--- Radius Neighbors ---"
from sklearn.neighbors import RadiusNeighborsClassifier
clf = RadiusNeighborsClassifier(radius=0.2)
execute(clf, "radius")

## Random Forest
print "--- Random Forest ---"
from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=10, criterion="entropy", min_samples_split=8)
execute(clf, "random_forest")

## AdaBoost
print "--- AdaBoost ---"
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier(n_estimators=20)
execute(clf, "adaboost")
