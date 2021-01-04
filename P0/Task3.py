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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def parta():
    phone_dict = {}
    for call in calls:
        if call[0] not in phone_dict:
            phone_dict[call[0]] = 1

        if call[1] not in phone_dict:
            phone_dict[call[1]] = 1

    for call in calls:
        if call[0] not in phone_dict:
            phone_dict[call[0]] = 1

        if call[1] not in phone_dict:
            phone_dict[call[1]] = 1

    code_list = {}
    for phone in list(phone_dict.keys()):
        if '(0' in phone:
            code_str = ''
            count = 0
            while ')' not in code_str:
                code_str += phone[count]
                count = count + 1

            if code_str not in code_list:
                code_list[code_str] = 1

        if '140' == phone[0:2]:
            if phone[0:2] not in code_list:
                code_list[phone[0:2]] = 1

        if ' ' in phone and ('7' == phone[0] or '8' == phone[0] or '9' == phone[0]):
            if phone[0:4] not in code_list:
                code_list[phone[0:4]] = 1

    sorted_code_list = sorted(list(code_list))
    print("The numbers called by people in Bangalore have codes:", sorted_code_list)
    return sorted_code_list


def partb():
    total_calls = 0
    total_fixed_line_calls = 0

    for call in calls:
        total_calls += 1
        if '(0' == call[0][0:2] and '(0' == call[1][0:2]:
            total_fixed_line_calls += 1

    percent = round(total_fixed_line_calls / total_calls * 100, 2)
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))
    return percent


parta()
partb()