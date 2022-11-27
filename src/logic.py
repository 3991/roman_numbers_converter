from number import number
import constant as c

def init():
    l = []

    l.append(number(c.I, 1))
    l.append(number(c.V, 5))
    l.append(number(c.X, 10))
    l.append(number(c.L, 50))
    l.append(number(c.C, 100))
    l.append(number(c.D, 500))
    l.append(number(c.M, 1000))

    return l

def get_arabic(nb):
    l = init()
    res = ''

    return res
