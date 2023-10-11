if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    m = max(arr)
    ls = [i for i in arr if i != m]
    print(max(ls))
