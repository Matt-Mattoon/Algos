# Given an array and a value Y, count and print the number of array values greater than Y.
def greater_than_y(arr, y):
    number_greater = 0
    for i in arr:
        if arr[i]>y:
            number_greater+=1
    print(f"greater_than_y() returned {number_greater}")
    return number_greater

greater_than_y([0,-3,5,5,5,4,3,2,1,-1], 4)