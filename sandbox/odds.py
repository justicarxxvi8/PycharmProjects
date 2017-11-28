list = []
calc = 0
def selectOdds(array, calc):
    while int(calc) < 20:
        list.append(calc)
        calc = int(calc) + 1
    for x in array:
        if x%3 == 0:
            print(x)





selectOdds(list, calc)