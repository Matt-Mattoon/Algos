# Function that finds the max value in an array and returns that value
def find_max(arr):
    print(f"find_max({arr})")
    if len(arr) == 0: # edge case
        print("list is empty")
        return
    max = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
    print(f"find_max returned {max}")
    return max

find_max([-3,0,6,3])
find_max([6])
find_max([])