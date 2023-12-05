# Replace any negative array values with 'Mert'.
def change_list(arr):
    for i in range(0, len(arr)):
        if arr[i] <= -1:
            arr[i] = "Mert"
    print(arr)
    return arr

change_list([-1,1,-1,1,-1])