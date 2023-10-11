# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

def find_repeating_character(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] and s[i].isalnum():
            return s[i]
    return -1

input_str = input()
result = find_repeating_character(input_str)
print(result)

