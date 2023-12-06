# Print all odd integers from 1 to 255.
def print_odds():
    print('print_odds')
    for i in range(1, 256):
        if i%2!=0:
            print(i)
    return

print_odds()