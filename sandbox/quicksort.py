input_array = [2,3,6,1,2,5,2,4,1,8]


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

print(quick_sort(input_array))