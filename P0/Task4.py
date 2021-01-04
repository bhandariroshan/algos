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
	telemarketers = {}
	incoming_call_dict = {}
	texts_phone_dict = {}

	for text in texts:
		if texts_phone_dict.get(text[0], None) == None:
			texts_phone_dict[text[0]] = 1

		if  texts_phone_dict.get(text[1], None) == None:
			texts_phone_dict[text[1]] = 1

	for call in calls:
		if incoming_call_dict.get(call[1], None) == None:
			incoming_call_dict[call[1]] = 1

	for call in calls:
		if incoming_call_dict.get(call[0], None) == None and texts_phone_dict.get(call[0], None) == None and telemarketers.get(call[0], None) == None:
			telemarketers[call[0]] = 1

	sorted_list =  sorted(list(telemarketers.keys()))
	return sorted_list

print("These numbers could be telemarketers: ", find_tele_marketers())