def quick_sort(array):
    lower = []
    pivots = []
    upper = []

    if len(array) > 0:
        pivot = array[0]
        for x in array:
            if x < pivot:
                lower.append(x)
            elif x > pivot:
                upper.append(x)
            elif x == pivot:
                pivots.append(x)#
        return quick_sort(lower) + pivots + quick_sort(upper)
    else:
        return array

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return found



input_array = [2,3,6,1,2,5,2,4,1,8]
sorted_list = quick_sort(input_array)
print(binarySearch(sorted_list, 8))
