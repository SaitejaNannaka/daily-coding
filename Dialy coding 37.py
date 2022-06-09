#Power Set: Power set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
If S has n elements in it then P(s) will have 2n elements

Example: 

Set  = [a,b,c]
power_set_size = pow(2, 3) = 8
Run for binary counter = 000 to 111

Value of Counter            Subset
   000                    -> Empty set
   001                    -> a
   010                    -> b
   011                    -> ab
   100                    -> c
   101                    -> ac
   110                    -> bc
   111                    -> abc



### python3 program for power set

import math;

def printPowerSet(set,set_size):
	
	# set_size of power set of a set
	# with set_size n is (2**n -1)
	pow_set_size = (int) (math.pow(2, set_size));
	counter = 0;
	j = 0;
	
	# Run from counter 000..0 to 111..1
	for counter in range(0, pow_set_size):
		for j in range(0, set_size):
			
			# Check if jth bit in the
			# counter is set If set then
			# print jth element from set
			if((counter & (1 << j)) > 0):
				print(set[j], end = "");
		print("");

# Driver program to test printPowerSet
set = ['a', 'b', 'c'];
printPowerSet(set, 3);

# This code is contributed by mits.

