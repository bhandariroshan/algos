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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def find_tele_marketers():
	telemarketers = set()
	incoming_call_set = set()
	texts_phone_set = set()

	for text in texts:
		texts_phone_set.add(text[0])
		texts_phone_set.add(text[1])

	for call in calls:
		incoming_call_set.add(call[1])

	for call in calls:
		if call[0] not in incoming_call_set and \
			call[0] not in texts_phone_set:
			telemarketers.add(call[0])

	sorted_list =  sorted(list(telemarketers))
	print("These numbers could be telemarketers: ")
	for each_number in sorted_list:
		print(each_number)
	return sorted_list

find_tele_marketers()
