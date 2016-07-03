import csv
import datetime
from event import event

# todo get until

# allevents events
allevents = []
with open('allevents.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    # list of events
    for row in reader:
        date_object = datetime.datetime.strptime(row['Time value'], '%b %d')
        date_object = date_object.replace(year=datetime.datetime.now().year)
        tmp_event = event(row['Title link'], date_object, row['Venue value'], img = row['Image'], moreURL = row['Title link_link']) 
        allevents.append(tmp_event)

# cyprusevents
with open('cyprusevents.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    # list of events
    for row in reader:
        # remove trailing strings after date
        date_substring = row['When'].split('th',1)[0].split('rd',1)[0].split('nd',1)[0].split('st',1)[0]
        date_object = datetime.datetime.strptime(date_substring , '%B %d')
        date_object = date_object.replace(year=datetime.datetime.now().year)
        # check if time is provided
        if row['Event time'] != "":
            #  parse time
            time_substring = row['Event time'].split(' ',1)[0]
            parsed_time =  datetime.datetime.strptime(time_substring , '%H:%M')
            # replace time
            date_object = date_object.replace(hour=parsed_time.hour)
            date_object = date_object.replace(minute=parsed_time.minute)
        tmp_event = event(row['Summary link'], date_object, row['Where value'], img = row['Image'], genre = row['Descriptionblock value'],moreURL = row['Summary link_link']) 
        allevents.append(tmp_event)

# MuicCy FB group
with open('musiccy.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    # list of events
    for row in reader:
        date_con = row['Month'] + ' ' + row['Day']
        date_object = datetime.datetime.strptime(date_con, '%b %d')
        date_object = date_object.replace(year=datetime.datetime.now().year)
        if row['Time'] != "":
            time_substring = row['Time'].split(' ', 1)[0] + " " + row['Time'].split(' ', 1)[1][0] + "M"
            parsed_time =  datetime.datetime.strptime(time_substring , '%I:%M %p')
            date_object = date_object.replace(hour=parsed_time.hour)
            date_object = date_object.replace(minute=parsed_time.minute)
        tmp_event = event(row['Event name/link'], date_object, row['Place'], moreURL = row['Event name/link_link']) 
        allevents.append(tmp_event)

#wherevent
with open('wherevent.csv', 'rb') as csvfile:
    reader = csv.DictReader(csvfile)
    # list of events
    for row in reader:
        date_object = datetime.datetime.strptime(row['Time'], '%H:%M')
        date_object = date_object.replace(year=datetime.datetime.now().year)
        tmp_event = event(row['Title/link'], date_object, row['Place'], img = row['Image'], moreURL = row['Title/link_link']) 
        allevents.append(tmp_event)

#  Sort all events by date
allevents = sorted(allevents, key=lambda event: event.m_time)
for i in allevents:
    print i.m_title
    print i.m_time
    print '==============='

# <h3>Monday 2nd June</h3>
                                
#                                 <h6>Starts at: 12:00 <b>Cycling</b></h6>
#                                 <p><i> Event Title Goes here.</i> </p>
#                                 <p><b>Location</b goes here</p>
#                                 <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto reiciendis eos magni
#                                   deleniti accusamus tempore, consectetur! Maxime amet, exercitationem nihil fugit eius esse
#                                   voluptatum ab incidunt minima, saepe reiciendis ipsum.</p>
#                                 <p><small>More: <a href="#">Link</a></small></p>

with open("pre.html") as f:
    with open("auto.html", "w") as f1:
        for line in f:
            f1.write(line) 

with open("auto.html", "a") as f1:
    for idx, i in enumerate(allevents):
        if(idx == 0 or allevents[idx-1].m_time.month != i.m_time.month):
            f1.write('<hr/>\n')
            f1.write('<h4>' + i.m_time.strftime("%A %b-%d at: %H:%M") + '</b></h4>\n')
        f1.write('<p><b>' + i.m_title + ' <small>-' + i.m_genre + '</small></b></p>\n')
        f1.write('<p><b>Location </b>' + i.m_place + '</p>\n')
        f1.write('<p>' + i.m_description + '</p>\n')
        f1.write('<p><small>More: <a href="' + i.m_detailsUrl + '">Link</a></small></p>\n')

with open("post.html") as f:
    with open("auto.html", "a") as f1:
        for line in f:
            f1.write(line) 

print "This line will be printed."

