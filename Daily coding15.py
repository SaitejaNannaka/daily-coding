
##Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.











import numpy as np
 
# initializing list
stream = [1, 4, 5, 2, 7]
 
# using random.choice() to
# get a random number
random_num = np.random.choice(stream)
 
# printing random number
print("random number is ",random_num)
