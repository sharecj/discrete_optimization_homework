#coding=utf8


def fibonacci(position):
    """
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...

    """
    if position == 1:
        return 0
    elif position == 2:
        return 1
    return fibonacci(position - 1) + fibonacci(position - 2)

if __name__ == '__main__':
    print fibonacci(40)
