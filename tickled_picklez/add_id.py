import csv

with open('20220926.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='|')
    line_count = 0
    for row in csv_reader:
        row.append(row[3].split('/')[-1])
        print("|".join(row))
