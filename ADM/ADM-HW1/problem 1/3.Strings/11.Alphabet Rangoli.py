def print_rangoli(n):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ls = []

    for i in range(n):
        substring = "-".join(alphabet[i:n])
        pattern_line = substring[::-1] + substring[1:]
        ls.append(pattern_line)

    max_width = len(ls[0])

    for i in range(n - 1, 0, -1):
        print(ls[i].center(max_width, '-'))

    for i in range(n):
        print(ls[i].center(max_width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)