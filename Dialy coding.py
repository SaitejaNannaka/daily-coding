#Daily Coding Problem-1

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k. For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Solution:-

def sum_num(list,k):
    total = set()
    
    for n in list:
        if x - n in total:
            return True
            
        total.add(n)
        
    return False
    
    
list=[10,15,3,7]
x=17
print(sum_num(list,x))
