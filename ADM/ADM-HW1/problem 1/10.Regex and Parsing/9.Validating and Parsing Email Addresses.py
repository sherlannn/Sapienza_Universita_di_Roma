# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    inp = input().split()
    name, email = inp[0], inp[1]
    
    if re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email):
        print(name,email)
