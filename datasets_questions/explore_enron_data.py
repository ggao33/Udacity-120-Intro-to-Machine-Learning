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
## part 1
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print("There are " + str(len(enron_data)) + " people in the dataset")

## part 2
no_features = enron_data["SKILLING JEFFREY K"].keys()
print("There are " + str(len(no_features)) +" features in each person")

## part 3
poi_cnt = 0
for k in enron_data.keys():
	if(enron_data[k]["poi"] == 1):
		poi_cnt += 1
print("There are " + str(poi_cnt) + " people of interest")

## part 4
import pandas as pd
df = pd.read_csv("../final_project/poi_names.txt")
print("There are　" + str(len(df)) + " poi in the name list")

## part 5
key_name = "Prentice James".upper()
print("James Prentice's total stock value is:")
print(enron_data[key_name]["total_stock_value"])

## part 6
key_name = "Colwell Wesley".upper()
print("How many poi receive emails from this Colwell Wesley?")
print(enron_data[key_name]["from_this_person_to_poi"])

## part 7
key_name = "Skilling Jeffrey K".upper()
print("What is the stock options exercised by Jeffrey K Skilling")
print(enron_data[key_name]["exercised_stock_options"])

## part 8
salary_cnt = 0
email_cnt = 0
for k,v in enron_data.items():
	if enron_data[k]["email_address"] != "NaN":
		email_cnt += 1
	if enron_data[k]["salary"] != "NaN":
		salary_cnt += 1

print("quantified salary #: " + str(salary_cnt))
print("known emails #: " + str(email_cnt))

## optional:
## part 9
total_payment_cnt = 0
for k,v in enron_data.items():
	if (enron_data[k]["total_payments"] == "NaN"):
		total_payment_cnt += 1
ans = total_payment_cnt / len(enron_data) * 100
print("NaN total payment percentage is: " + str(ans) + " %")

## part 10
poi_tp_cnt = 0
for k,v in enron_data.items():
	if (enron_data[k]["total_payments"] == "NaN") & (enron_data[k]["poi"] == 1):
		poi_tp_cnt += 1
ans = poi_tp_cnt / 18 * 100
print("NaN total payment percentage is: " + str(ans) + " %")

## part 11
print("New number of people in the dataset is " + str(len(enron_data) + 10))
print("New NaN total payment number is: " + str(total_payment_cnt + 10))

## part 12
print("New number of POI is " + str(poi_cnt + 10))
print("New number of NaN total payment is: " + str(poi_tp_cnt + 10))