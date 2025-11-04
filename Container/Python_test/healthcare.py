import sys
import csv
from pymongo import MongoClient
import pandas as pd

# MongoDB connection
client = MongoClient('mongodb://dev:dev@host.docker.internal', 27016)
db = client['test']
collection = db['collHealthCare']

csvDataFrame = pd.read_csv("healthcare_dataset.csv", dtype = str)

mongoDbDataFrame = pd.DataFrame(list(db.collHealthCare.find({})))
mongoDbDataFrame = mongoDbDataFrame.drop('_id', axis=1)

#Comparaison du nombre de lignes
assert csvDataFrame.shape[0] == mongoDbDataFrame.shape[0], "il n'y a pas le même nombre de lignes"

#Comparaison du nombre de colonnes
assert csvDataFrame.shape[1] == mongoDbDataFrame.shape[1], "il n'y a pas le même nombre de colonnes"

#Comparaison de toutes les célulles
errors = []
for line in range(0, 1000) :
    for column in range (0, mongoDbDataFrame.shape[1]) :
        if not str(csvDataFrame.iloc[line, column]) == str(mongoDbDataFrame.iloc[line, column]) :
            errors.append("line : " + str(line) + " - " + "column : " + str(column) + " -------- " + str(csvDataFrame.iloc[line, column]) + " -------- " + str(mongoDbDataFrame.iloc[line, column]))
assert not errors, "errors occured:\n{}".format("\n".join(errors))

print("script terminé")
