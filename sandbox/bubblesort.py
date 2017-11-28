def bubblesort(a):
    for x in range(len(a)-1):
        if a[x] > a[x+1]:
            temp = a[x]
            next = a[x+1]
            a[x+1] = temp
            a[x] = next
    return a



array = [2,4,1,5,6,8,3,2]

for x in range(len(array)-1):
    z = bubblesort(array)

print(z)