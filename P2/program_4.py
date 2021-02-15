# Dutch National Flag Problem
# Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal. 
# You're not allowed to use any sorting function that Python provides.

# Note: O(n) does not necessarily mean single-traversal. For e.g. 
# if you traverse the array twice, that would still be an O(n) solution but it will not count as single traversal.

# Here is some boilerplate code and test cases to start with:

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    # initialize pointers for next positions of 0 and 2
    cursor = 0
    start_index_0 = 0
    start_index_2 = len(input_list) - 1

    count = 0
    while cursor <= start_index_2: 
        count += 1
        if input_list[cursor] == 0:
            input_list[cursor] = input_list[start_index_0]
            input_list[start_index_0] = 0
            cursor += 1
            start_index_0 += 1

        elif input_list[cursor] == 2:
            input_list[cursor] = input_list[start_index_2]
            input_list[start_index_2] = 2
            start_index_2 -= 1

        else:
            cursor += 1

    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([0, 0, 0, 0, 0, 0, 1])
test_function([1, 0, 0, 0, 0, 0, 1])
test_function([2,2,2,2,2,1])
test_function([])