#coding=utf8

table = {}

def fibonacci(position):
    """
    0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144 ...

    """
    if position in table:
        return table[position]

    if position == 1:
        return 0
    elif position == 2:
        return 1

    table[position] = fibonacci(position - 1) + fibonacci(position - 2)
    return table[position]

if __name__ == '__main__':
    print fibonacci(40)
