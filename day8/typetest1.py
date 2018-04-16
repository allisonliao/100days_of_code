import colorama


def erase_display():
    print('\x1b[2J', end="")


def cursor_pos(x, y):
    if x < 1:
        x = 1

    if y < 1:
        y = 1

    print('\x1b[{};{}H'.format(x, y), end='')


def main():
    colorama.init()
    erase_display()
    cursor_pos(3, 3)
    print('hello')


if __name__ == '__main__':
    main()