#Power Set: Power set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
If S has n elements in it then P(s) will have 2n elements

Example: 

Set  = [a,b,c]
power_set_size = pow(2, 3) = 8



#Python program to find powerset
from itertools import combinations
def print_powerset(string):
	for i in range(0,len(string)+1):
		for element in combinations(string,i):
			print(''.join(element))
string=['a','b','c']
print_powerset(string)

