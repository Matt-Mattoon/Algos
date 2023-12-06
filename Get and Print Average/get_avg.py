# Analyze a list’s values and print the average.
def get_avg(li):
    total = 0
    print('get_avg')
    for val in li:
        total+=val
    avg = total/len(li)
    print('returned', avg)
    return avg

get_avg([8,8,5,7])