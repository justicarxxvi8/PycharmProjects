def merge(left, right):
    result = []
    i ,j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def mergesort(list):
    if len(list) < 2:
        return list
    middle = int(len(list) / 2)
    left = mergesort(list[:middle])
    right = mergesort(list[middle:])
    return merge(left, right)

print(mergesort([5,1,9,2,6]))