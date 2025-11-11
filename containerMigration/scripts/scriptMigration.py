import sys
import csv
import os
from pymongo import MongoClient

# MongoDB connection

login = os.environ["TECHNIQUEMIGRATIONLOGIN"]
password = os.environ["TECHNIQUEMIGRATIONPASSWORD"]

client = MongoClient('mongodb://' + login + ':' + password + '@host.docker.internal', 27016)
db = client['test']
collection = db['collHealthCare']
# CSV file path
csv_file_path = "/dataToMigrate/healthCare.csv"
# Insertion des données
with open(csv_file_path, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        collection.insert_one(row)

print("script terminé")
sys.exit()