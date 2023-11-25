# Create an array with all the odd integers between 1 and num parameter (inclusive).
def odd_list(num):
    print(f"odd_list({num})")
    new_list = []
    for i in range(num+1):
        if i%2 != 0:
            new_list.append(i)
    print(f"odd_list() returned {new_list}")
    return new_list

odd_list(37)