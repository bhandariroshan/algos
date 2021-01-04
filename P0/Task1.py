"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def find_phone_list():
	phone_numbers  = {}

	for text in texts:
		if phone_numbers.get(text[0], None) == None:
			phone_numbers[text[0]] = 1 

		if phone_numbers.get(text[1], None) == None:
			phone_numbers[text[1]] = 1 

	for call in calls:
		if phone_numbers.get(call[0], None) == None:
			phone_numbers[call[0]] = 1 

		if phone_numbers.get(call[1], None):
			phone_numbers[call[1]] = 1 

	print ('There are {} different telephone numbers in the records.'.format(len(list(phone_numbers.keys()))))

find_phone_list()