def adjacentElementsProduct(inputArray):
    result = []

    for x in range(len(inputArray)-1):

        output = inputArray[x] * inputArray[x+1]
        result.append(output)
    print(max(result))
    return max(result)


def adjacentElementsProductSmall(array):
    return max(array[x] * array[x+1] for x in range(len(array)-1))

print(adjacentElementsProductSmall([4,1,2,2,3,4,6,5]))


"""
function adjacentElementsProduct($inputArray) {
for($x = 0; $x < sizeof($inputArray)-1; $x++){
$results[] = $inputArray[$x]*$inputArray[$x+1];
}
rsort($results);

return $results[0];
}

"""