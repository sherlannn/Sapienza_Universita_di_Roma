# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    num = "".join(input())
    if re.match(r'^[456][\d]{3}-?[\d]{4}-?[\d]{4}-?[\d]{4}$', num) and not re.search(r'(\d)\1{3,}', num.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")
