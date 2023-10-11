def mutate_string(string, position, character):
    s1 = string[:position]
    s2 = string[position+1:]
    return s1+character+s2

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)