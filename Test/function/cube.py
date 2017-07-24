def cube(number):
    print "%d" % (number ** 3)


def by_three(number):
    if number % 3 == 0:
        cube(number)

    else:
        return False
