# A function, with a parameter int, that will print the consecutive sum of 0 to int and return the sum
def consecutive_sum(int):
    total = 0
    for i in range(int+1):
        total += i
        print(f"+ {i} = {total}")
    print(f"consecutive_sum returned {total}")
    return total

consecutive_sum(255)