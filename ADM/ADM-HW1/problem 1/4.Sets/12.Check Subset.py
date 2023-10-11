# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
for i in range(n):
    a = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))

    print("True" if len(set_a - set_b) == 0 else "False")
