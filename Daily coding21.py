
##Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

##For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

solution:-


def time_period(x):
    count_of_time = [ 0 for i in range(1000)]
    for a in x:
        count_of_time[a[0]] += 1
        count_of_time[a[1]] += -1
    rooms =0
    temp = 0
    for a in count_of_time:
        temp +=a
        if(temp >rooms):
            rooms = temp
    return rooms
print(time_period([[30,75],[0,50],[60,150]]))
print(time_period([]))
