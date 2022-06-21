##cons(a,b) constructs a pair , and car(pair) and cdr(pair)
returns first element and last element of the pair . For example , 
car(cons(3,4)) returns 3,
and cdr(cons(3,4)) returns 4
Implement car and cdr
####defining the inner functions is the solution for this problem





solution:-

def cons(x,y):
    def pair(f):
        return f(x,y)
    return pair
def car(pair):
    def first_element(x,y):
        return x
    return pair(first_element)
def cdr(pair):
    def second_element(x,y):
        return y
    return pair(second_element)
print(car(cons(3,4)))
print(cdr(cons(3,4)))
