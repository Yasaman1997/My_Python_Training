def max_of_three(a, b, c):
    max_3 = 0
    if a > b:
        # max_3=a
        if a > c:
            max_3 = c
        else:
            max_3 = a
    else:
        if b > c:
            max_3 = b
        else:
            max_3 = c
    return max_3


print  max_of_three(2,5,87)