#!/usr/bin/python3
import sys
from logic import get_arabic
from controls import command_line_arguments


if __name__ == '__main__':
    nb = command_line_arguments()

    result = get_arabic(nb)

    print(result)
