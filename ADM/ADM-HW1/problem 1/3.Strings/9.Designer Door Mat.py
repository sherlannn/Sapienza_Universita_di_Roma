# Enter your code here. Read input from STDIN. Print output to STDOUT

n = input()
ls = n.split()
h, l = int(ls[0]), int(ls[1])

i = 0
while i < h // 2:
    mask = '.|.' * (i * 2 + 1)
    print(mask.center(l, '-'))
    i += 1


print('WELCOME'.center(l, '-'))

i = h // 2 - 1
while i >= 0:
    mask = '.|.' * (i * 2 + 1)
    print(mask.center(l, '-'))
    i -= 1
