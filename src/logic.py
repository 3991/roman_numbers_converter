from number import Number
import constant as c

def init():
    l = []

    l.append(Number(c.I, 1))
    l.append(Number(c.V, 5))
    l.append(Number(c.X, 10))
    l.append(Number(c.L, 50))
    l.append(Number(c.C, 100))
    l.append(Number(c.D, 500))
    l.append(Number(c.M, 1000))

    return l


def get_arabic(nb):
    l = init()
    res = ''
    l = l[::-1]

    i = 0

    while nb != 0:
        if nb == l[i].get_arabic():
            res = res + l[i].get_roman()
            break;
        elif nb > l[i].get_arabic():
            res = res + l[i].get_roman()
            nb = nb - l[i].get_arabic()

        if not(nb >= l[i].get_arabic()):
            if i < len(l)-1:
                i += 1
    return res
