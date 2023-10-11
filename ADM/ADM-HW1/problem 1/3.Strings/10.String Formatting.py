def print_formatted(num):
    
    width = len("{0:b}".format(num))

    for i in range(1, num + 1):
        decimal = "{0:{width}d}".format(i, width=width)
        octal = "{0:{width}o}".format(i, width=width)
        hexadecimal = "{0:{width}X}".format(i, width=width)
        binary = "{0:{width}b}".format(i, width=width)

        print(f"{decimal} {octal} {hexadecimal} {binary}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)