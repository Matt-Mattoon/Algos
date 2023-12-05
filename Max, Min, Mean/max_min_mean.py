# Given an array, print the max, min and average values for that array.
def mmm(arr):
    arr_max = arr[0]
    arr_min = arr[0]
    total = arr[0]
    avg = 0
    for i in range(1, len(arr)):
        total += arr[i]
        if arr[i]>arr_max:
            arr_max = arr[i]
        if arr[i]<arr_min:
            arr_min = arr[i]
    avg = total/len(arr)
    print(f"max {arr_max}, min {arr_min}, avg {avg}")
    return arr_max, arr_min, avg

mmm([-5,-5,3,4,1,2,5,5])


