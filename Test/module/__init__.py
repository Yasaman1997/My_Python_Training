from math import abs


def distance_from_zero(me):
    if type(me) == int or type(me) == float:
        return abs(me)

    else:
        return " Nope"