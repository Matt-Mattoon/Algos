# A Narcissistic Number is a positive number which is the sum of
# its own digits, each raised to the power of the number of digits
# in a given base. In this Kata, we will restrict ourselves to decimal (base 10).
# For example, take 153 (3 digits), which is narcisstic:
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

def narcissistic(num):
    sum = 0
    for digits in str(num):
        sum = sum + (int(digits) ** len(str(num)))
    if sum == num:
        return True
    else:
        return False

print(narcissistic(153))
