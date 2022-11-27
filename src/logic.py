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
