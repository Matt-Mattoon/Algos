# Iterate through a given array, printing each value.
def print_list(li):
    print('print_array')
    for i in range(len(li)):
        val = li[i]
        print(i, val)
    return

print_list(['Mert','was','here.'])