# Time Complexity

In this program I am using the concept of binary search. I start by assigning low variable as 0 and high variable as the number. Then I calculate the mid value of them and I check if the square of the mid is greater than or smaller than the number. I keep repeating this process until we start seeing convergence i.e the mid point remains same. Everytime I calculate mid and set the direction to one half, I am reducing my search space to half. Hence the overall time complexity of this problem is O(nlogn).

# Space Complexity

The program uses 3 variables high, low, mid and old_mid. Other than that there are no arrays and any other data structure. As such the space complexity of the code is O(1).