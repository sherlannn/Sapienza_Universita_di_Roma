cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    ls = [0, 1]
    if n < 2:
        return ls[:n]
    for i in range(2, n):
        ls.append(ls[i - 1] + ls[i - 2])
    return ls

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))