# O(log2N)
def insert_sorted(arr, x):
    # Binary search to find the index where x should be inserted
    low, hight = 0, len(arr)
    while low < hight:
        mid = (low + hight) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            hight = mid
    
    # Insert x at the correct position
    arr.insert(low, x)