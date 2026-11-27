import csv
import json

with open("data.csv", "r", encoding="utf-8", newline = "") as file:
    csv_reader = csv.DictReader(file)



