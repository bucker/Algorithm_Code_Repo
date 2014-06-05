# Count the number of inversions in the file
# Ans: 2407905288

def NumberOfInversions(intArray, n):
    if n == 0:
        return []
    if n == 1:
        return intArray
    A = NumberOfInversions(intArray[:n // 2], n // 2)
    B = NumberOfInversions(intArray[n // 2:], n - (n // 2))
    D = merge(A, B)
    return D

def merge(aArray, bArray):
    global count
    aIndex = 0
    bIndex = 0
    aSize = len(aArray)
    bSize = len(bArray)
    resultArray = []

    if aSize == 0:
        return bArray
    elif bSize == 0:
        return aArray

    for i in range(aSize + bSize):
        if aArray[aIndex] <= bArray[bIndex]:
            resultArray.append(aArray[aIndex])
            aIndex += 1
        else:
            resultArray.append(bArray[bIndex])
            bIndex += 1
            count += (aSize - aIndex)
        if aIndex >= aSize:
            aArray.append(9999999999)
        if bIndex >= bSize:
            bArray.append(9999999999)
    return resultArray

file_name = "IntegerArray.txt"
int_array = []
count = 0
# store each line into a list
with open(file_name) as f:
    for line in f:
        int_array.append(int(line))

NumberOfInversions(int_array, len(int_array))

print count