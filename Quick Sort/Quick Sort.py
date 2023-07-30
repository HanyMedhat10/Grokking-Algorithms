# O(N log(N)) best case and average case
#  O(N**2)=(N*N) worst case 
# import numpy as np
def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [element for element in array[1:] if element <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less)+ [pivot] + quickSort(greater)

print(quickSort([10,5,2,3]))
# arr = np.random.randint(0, 100, size=50)
# print(arr)
# print(quickSort(arr))