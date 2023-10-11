# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

inp = input()
inp2 = input()


match_ls = list(re.finditer(fr'(?={re.escape(inp2)})', inp))

if match_ls:
    # Print the start and end positions of each match
    for match in match_ls:
        start = match.start()
        end = start + len(inp2) - 1
        print((start, end))
else:
    print((-1, -1))
