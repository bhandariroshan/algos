# Time Complexity of rotated_array_search (main code of this program)

Again in this problem, I use concept of binary search. However instead of thinking the array as sorted, I think of position of 2 sequences i.e increasing sequence or decreasing sequence seperated by midpoint.  

First, Inside the while loop, first if the mid element is the element searched for or not is checked. If it the searched element then the mid point is returned.

Second If statement, checks if the first half is an increasing sequence and if the searched element lies in that sequence or not. To determine if the sequence is increasing we check if the first second element is greater than the second element or not. If the sequence is increasing and the element is greater than the first element and smaller than the midpoint element, then the last is updated to be the mid and then in next iteration we check the array elements in that sequence only. 

Following Elif statement checks if the first sequence before the mid point is decreasing sequence and also checks if the element falls in that sequence. If it is true, then it updates last as mid and in next loop, looks only in that sequence. 

Final else statement is evaluated only for the case where the number looked for does not fall in the first sequence. As such we update the first to be mid + 1 and check on the remaining sequence.

This way, everytime we look for solution, we are reducing the search space to half or by some fraction times the original. Hence the overall complexity of the algorithm is O(nlog(n)).

# Space Complexity of rotated_array_search
For this program, I am 3 variables, first, mid and last. Other than that there is not any other variables or data structures used. As such the space complexity of the code is constant i.e O(1).