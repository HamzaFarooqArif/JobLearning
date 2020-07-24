import csv

'''
with open('Desktop/JobLearning/LearningDocuments/csvReader/file.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

'''

with open("Desktop/JobLearning/LearningDocuments/csvReader/file.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))