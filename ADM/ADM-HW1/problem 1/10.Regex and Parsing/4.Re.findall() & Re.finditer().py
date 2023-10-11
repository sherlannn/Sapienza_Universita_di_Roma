# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

c = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
v = 'AEIOUaeiou'

if __name__ == "__main__":
    
    inp = input()
    
    res = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), inp)
    res = "\n".join(res or ['-1'])
    print(res)
