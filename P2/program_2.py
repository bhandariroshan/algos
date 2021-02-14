# Search in a Rotated Sorted Array
# You are given a sorted array which is rotated at some random pivot point.

# Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You can assume there are no duplicates in the array and your algorithm's runtime complexity must be in the order of O(log n).

# Example:

# Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

# Here is some boilerplate code and test cases to start with:

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    if not input_list:
        return -1

    last = len(input_list)-1
    first = 0
    mid = (first+last) // 2
    while input_list[mid] != number:

        if number == input_list[mid]:
            return mid
        
        # If the numebr is in the left and if it is increasing
        if input_list[first] <= input_list[first+1] and number >= input_list[first] and number <= input_list[mid-1]:
            last = mid-1

        # If the number is in the left and if it is decreasing
        elif input_list[first] > input_list[first+1] and number >= input_list[mid-1] and number <= input_list[first]:
            last = mid - 1

        else:
            first = mid + 1

        mid = (first+last) // 2
        if first >= last and input_list[mid] != number:
            return -1

    return mid


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[], 8])
test_function([[8], 8])