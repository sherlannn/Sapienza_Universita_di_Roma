import re

n = int(input())

for _ in range(n):
    line = input()
    modified_line = re.sub(r'(?<= )(&&|\|\|)(?= )', lambda match: "and" if match.group(0) == "&&" else "or", line)
    print(modified_line)
