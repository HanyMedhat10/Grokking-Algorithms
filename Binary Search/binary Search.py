# complexity O(log2n) -> Binary Search  result max step program sec
# complexity O(n) -> simple search      result max step program sec
list = range(1,101)
print(len(list))
item = int(input("Enter number "))
low = 0
hight = len(list)-1
while low <= hight:
    mid = (low + hight) // 2
    guess = list[mid]
    if guess == item :
        print("to get item")
        break
    elif guess > item:
        hight = mid - 1
        print(f"wait not get item {mid} ")
    else:
        low = mid + 1

# create function binary Search 
def binary_search(list,item):
    low = 0
    hight = len(list)-1
    while low<=hight:
        mid = (low+hight) // 2
        guess = list[mid]
        if guess == item:
            return item 
        elif guess > item:
            hight = mid -1
        else:
            low = mid + 1
    return None




