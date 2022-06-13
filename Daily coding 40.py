#Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.

For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.




def getSingle(arr, n):
	ones = 0
	twos = 0
	
	for i in range(n):
		
		twos = twos ^ (ones & arr[i])

		ones = ones ^ arr[i]
		
		common_bit_mask = ~(ones & twos)

		ones &= common_bit_mask

		twos &= common_bit_mask
	return ones
	
# driver code
arr = [6, 1, 3, 3, 3, 6, 6]
n = len(arr)
print("The element with single occurrence is ",
		getSingle(arr, n))


