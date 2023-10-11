# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    number = input()
    p = '^[789][0-9]{9}$'
    print("YES" if bool(re.match(p, number)) else "NO")
