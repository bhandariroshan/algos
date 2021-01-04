"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)



"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def find_max():
	max_duration = None
	phone = None
	for call in calls:
		if not max_duration or call[3] > max_duration:
			max_duration = call[3]
			phone = call[0]
	print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone, max_duration))

find_max() 