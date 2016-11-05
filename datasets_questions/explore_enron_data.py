#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "number of people: ", len(enron_data)

print "number of features per person: ", len(enron_data["GLISAN JR BEN F"])

### number of people with POI
people_with_poi = 0
for person_name in enron_data:
    if enron_data[person_name]["poi"] == 1:
        people_with_poi += 1
print "number of people with POI: ", people_with_poi

print "total value of stock belonging of James Prentice: ", enron_data["PRENTICE JAMES"]["total_stock_value"]

print "number of email messages from Wesley Colwell to persons of interest: ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "value of stock options exercised by Jeffrey K Skilling: ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

print "Jeffrey Skilling payments: ", enron_data["SKILLING JEFFREY K"]["total_payments"]
print "Andrew Fastow payments: ",enron_data["FASTOW ANDREW S"]["total_payments"]
print "Ken Lay payments: ",enron_data["LAY KENNETH L"]["total_payments"]

### people with known salary
people_with_salary = 0
for person_name in enron_data:
    if not isinstance(enron_data[person_name]["salary"], basestring):
        people_with_salary += 1
print "people with known salary: ", people_with_salary

### people with known email address
people_with_email_address = 0
for person_name in enron_data:
    if not enron_data[person_name]["email_address"] == "NaN":
        people_with_email_address += 1
print "people with known email address: ", people_with_email_address

### helper functions to convert from dict to numpy array
# featureFormat() and targetFeatureSplit() in tools/feature_format.py

### number of people have "NaN" for their total payments
people_without_total_payments = 0
for person_name in enron_data:
    if enron_data[person_name]["total_payments"] == "NaN":
        people_without_total_payments += 1
print "percentage of people have \"NaN\" for their total payments: ", people_without_total_payments /  float(len(enron_data)) * 100

### number of POIs have "NaN" for their total payments
pois_without_total_payments = 0
for person_name in enron_data:
    if enron_data[person_name]["total_payments"] == "NaN" and enron_data[person_name]["poi"] == 1:
        pois_without_total_payments += 1
print "percentage of POIs have \"NaN\" for their total payments: ", pois_without_total_payments / float(people_with_poi) * 100
