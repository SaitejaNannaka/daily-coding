
##Given an array of numbers, find the maximum sum of any contiguous subarray of the array.
For example, given the array [34, -50, 42, 14, -5, 86], the maximum sum would be 137, 
since we would take elements 42, 14, -5, and 86.
Given the array [-5, -1, -8, -9], the maximum sum would be 0, since we would not take any elements.
Do this in O(N) time.





solution:-

def sum_of_array(array):

    max_sub_array = 0
    sum1 = 0
    for i in range(len(array)):
        for j in range(len(array)+1):
            sum1= sum(array[i:j])

            max_sub_array = max(max_sub_array,sum1)
    return max_sub_array

print(sum_of_array( [34, -50, 42, 14, -5, 86]))

print(sum_of_array([-5, -1, -8, -9]))
