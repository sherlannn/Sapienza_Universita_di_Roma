# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    pattern = r"(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})"
    res = re.findall(pattern, input())
    for r in res:
        print(r)
