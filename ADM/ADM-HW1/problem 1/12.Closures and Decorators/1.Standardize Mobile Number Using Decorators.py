def wrapper(f):
    def fun(l):
        out = []
        for t in l:
            b = t[-10:]
            res = '+91 {} {}'.format(b[:5], b[5:])
            out.append(res)
        f(out)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


