#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn import cross_validation
from collections import Counter
import numpy

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)

### your code goes here

features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(features, labels, test_size=0.3, random_state=42)

clf = DecisionTreeClassifier()
clf.fit(features_train, labels_train)

pred = clf.predict(features_test)
#print accuracy_score(pred, labels_test)
#print Counter(pred)
#print accuracy_score(numpy.zeros(29), labels_test)
#print precision_score(labels_test, pred)
print recall_score(labels_test, pred)

truePositives = 0
for i in range(0, len(pred)):
    if pred[i] == 1 and pred[i] == labels_test[i]:
        ++truePositives
#print "True positives: ", truePositives

#predictions = [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1]
#true_labels = [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0]
# tp = 6
# tn = 9
# fp = 3
# fn = 2
# prec = 0.66
# rec = 0.75
