# Enter your code here. Read input from STDIN. Print output to STDOUT

m = int(input())
input_data = input()
elements_a = input_data.split()
a = set(map(int, elements_a))

n = int(input(""))
input_data = input()
elements_b = input_data.split()
b = set(map(int, elements_b))

sorted_result = sorted(list(a.symmetric_difference(b)))

for i in sorted_result:
    print(i)
