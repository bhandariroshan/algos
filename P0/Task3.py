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
    codes = set()
    for call in calls:
        if not call[0].startswith('(080)'):
            continue

        if call[1].startswith('(0'):
            code_str = ''
            index = 0
            while ')' not in code_str:
                code_str += call[1][index]
                index = index + 1

            code_str = code_str[1:-1]
            codes.add(code_str) 

        if call[1].startswith('140'):
            codes.add('140') 

        if ' ' in call[1] and ('7' == call[1][0] or '8' == call[1][0] or '9' == call[1][0]):
            codes.add(call[1][0:4])

    sorted_code_list = sorted(list(codes))
    print("The numbers called by people in Bangalore have codes:")
    for each_code in sorted_code_list:
        print(each_code)
    return sorted_code_list


def partb():
    total_calls = 0
    total_fixed_line_calls = 0

    for call in calls:
        if call[0].startswith('(080)'):
            total_calls += 1
            if call[1].startswith('(080)'):
                total_fixed_line_calls += 1

    percent = round(total_fixed_line_calls / total_calls * 100, 2)
    print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percent))
    return percent


parta()
partb()