# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

for _ in range(int(input())):
    uid = input()
    if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})(?=[a-zA-Z0-9]{10}$)', uid):
        print("Valid")
    else:
        print("Invalid")
