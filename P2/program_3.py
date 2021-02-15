# Rearrange Array Elements
# Rearrange Array Elements so as to form two number such that their sum is maximum. 
# Return these two numbers. You can assume that all array elements are in the range [0, 9]. 
# The number of digits in both the numbers cannot differ by more than 1. 
# You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

# for e.g. [1, 2, 3, 4, 5]

# The expected answer would be [531, 42]. Another expected answer can be [542, 31]. 
#  In scenarios such as these when there are more than one possible answers, return any one.

# Here is some boilerplate code and test cases to start with:

def merge(left, right):
    first = None
    second = None
    result = []
    while len(left)>0 or len(right) > 0:
        if first is None and len(left) > 0:
            first = left.pop(0)

        if second is None and len(right) > 0:
            second = right.pop(0)

        if first is not None  and second is not None:
            if first >= second:
                result.append(second)
                second = None
        
            else:
                result.append(first)
                first = None

        if first is not None and len(right) == 0:
            result.append(first)
            first = None

        if second is not None and len(left) == 0:
            result.append(second) 
            second = None

    return result

def sort_array(array):
    if len(array) == 1:
        return array

    else:
        mid = len(array) // 2
        left = sort_array(array[0:mid])
        right = sort_array(array[mid:])

        return merge(left, right)

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if not input_list:
        return []

    sorted_array = sort_array(input_list)
    one = 0
    two = 0

    one_pow = 0
    two_pow =0

    for count, elem in enumerate(sorted_array):
        if count % 2 == 0:
            one += elem * 10 ** one_pow
            one_pow += 1
        else:
            two += elem * 10 ** two_pow
            two_pow += 1

    solution = [one, two]
    return solution

    # for i in range(0, len(sorted_array)):


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [531, 42]]) 
test_function( [[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[], []])
test_function([[0,0,9,1,0], [910,0]])
test_function([[5,5,5], [55,5]])
test_function([[1,2], [1, 2]])
test_function([[1], [1]])