import sys
import csv
from pymongo import MongoClient

# MongoDB connection
client = MongoClient('mongodb://dev:dev@host.docker.internal', 27016)
db = client['test']
collection = db['collHealthCare']

# CSV file path
csv_file_path = "healthcare_dataset.csv"

# Insertion des données
with open(csv_file_path, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        collection.insert_one(row)

print("script terminé")
sys.exit()
