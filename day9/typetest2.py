import sys
import os
import msvcrt
import colorama


def erase_display():
    print('\x1b[2J', end="")


def cursor(x, y, txt):
    print('\x1b[{};{}H{}'.format(y, x, txt), end='')


def main():
    colorama.init()
    erase_display()

    x_pos = 1
    y_pos = 1

    txt = None
    while txt != '\x1b':
        txt = msvcrt.getch().decode('utf8')
        cursor(1, 40, '\x1b[31m' + str(x_pos) + '\x1b[0m')
        cursor(x_pos, y_pos, txt)

        x_pos += 1


if __name__ == '__main__':
    main()
