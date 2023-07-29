#  Selection Sort O(n**2/2 + n/2)
arr = [3,8,5,2]
def findSmallest(arr):
    smallest = arr[0]
    smallestIndex = 0
    for i in range(1,len(arr)):
        if arr[i] < smallest:
            smallest=arr[i]
            smallestIndex = i
    return smallestIndex

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallestIndex = findSmallest(arr)
        newArr.append(arr.pop(smallestIndex))
    return newArr