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
    phone_call = {}
    for call in calls:
        phone_call[call[0]] = phone_call.get(call[0] , 0) + float(call[3])
        phone_call[call[1]] = phone_call.get(call[1] , 0) + float(call[3])

    phone_call_list = []
    for each_key in phone_call:
        phone_call_list.append({'phone': each_key, 'duration': phone_call[each_key]})

    sorted_phone_calls = sorted(phone_call_list, key=lambda i: i['duration'], reverse=True)
    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
            sorted_phone_calls[0]['phone'], 
            sorted_phone_calls[0]['duration']
        )
    )

find_max() 