def is_sorted(l):
    return all(a <= b for a, b in zip(l[:-1], l[1:]))

def bubblesort(a):
    for x in range(len(a)-1):
        if a[x] > a[x+1]:
            temp = a[x]
            a[x] = a[x+1]
            a[x+1] = temp
    if is_sorted(a):
        print(a)
    else:
        return bubblesort(a)

array = [2,4,1,5,6,8,3,2]
bubblesort(array)

