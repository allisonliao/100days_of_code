import sys
import os
import msvcrt
import colorama
from termcolor import colored


txt = "tHe FOx juMpED iNTo tHe HoLE aNd DieD."
err = ''

def erase_display():
    print('\x1b[2J', end="")


def cursor(x, y, txt):
    print('\x1b[{};{}H{}'.format(y + 1, x + 1, txt), end='')


def main():
    colorama.init()
    erase_display()

    x_pos = 0
    y_pos = 0

    cursor(x_pos, y_pos, txt)
    cursor(x_pos, 9, '')

    while True:
        ch = msvcrt.getch().decode('utf8')
        if ch == '\x1b' or x_pos == len(txt):
            break

        if ch == '\b':
            if x_pos != 0:
                x_pos -= 1
                cursor(x_pos, y_pos, txt[x_pos])
                cursor(x_pos, 9, ' \b')
                # cursor(x_pos, 9, '')

        elif ch == txt[x_pos]:
            cursor(x_pos, y_pos, ch)
            cursor(x_pos, 9, colored(ch, 'red'))
            x_pos += 1

        else:
            cursor(x_pos, y_pos, colored(txt[x_pos], 'red'))
            cursor(x_pos, 9, ch)  #  + '\a'
            x_pos += 1



if __name__ == '__main__':
    main()
