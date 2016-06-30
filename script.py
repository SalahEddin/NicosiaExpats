import csv
import datetime

with open('allevents.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print row['Title link_link']
        dateString = row['Time value']
        date_object = datetime.datetime.strptime(dateString, '%b %d')
        date_object = date_object.replace(year=2016)
        print date_object
        # print 'Where: ' + row['Venue value']
print "This line will be printed."