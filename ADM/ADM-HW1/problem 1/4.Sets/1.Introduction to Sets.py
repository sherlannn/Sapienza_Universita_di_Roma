def average(array):
    # your code goes here
    length = len(set(array))
    summ = sum(set(array))
    return summ/length

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)