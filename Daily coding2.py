#Dialy coding

#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].


#Solution:-


input_list = [3,2,1]

def compute(a_list):
    list = []

    for i, v in enumerate(a_list):
        original_list = a_list
        original_int = original_list[i]
        original_list[i] = 1

        result = 1
        for x in original_list:
            result = result * x

        list.append(result)

        original_list[i] = original_int

    return list

z = compute(input_list)
print(z)
