# Ehsan Mokhtari - ehsan76m@gmail.com
# Problem 1 Solutions

#########################################

##### Introduction (https://www.hackerrank.com/domains/python/py-introduction)

##### 1.Say Hello, World! With Python
print("Hello, World!")


#### 2.Python If-Else
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print("Weird")
    elif n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")


##### 3.Arithmetic Operators
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    #first line output
    print(a+b)
    
    #second line output
    print(a-b)
    
    #third line output
    print(a*b)
	

##### 4.Python Division
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    #first line output
    print(a//b)
    
    #2nd line output
    print(a/b)


##### 5.Loops
if __name__ == '__main__':
    n = int(input())
    if n==0:
        print(0)
    elif  n>0:   
        for i in range(n):
            print(i**2) 


##### 6.Write a function
def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

year = int(input())
print(is_leap(year))


##### 7.Print Function
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i+1, end="") 

###################################################################

##### Data types (https://www.hackerrank.com/domains/python/py-basic-data-types)

##### 1.List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    ls = [ [i, j, k]
    for i in range(x + 1)
    for j in range(y + 1)
    for k in range(z + 1)
    if i + j + k != n ]
    
    print(ls)


##### 2.Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    m = max(arr)
    ls = [i for i in arr if i != m]
    print(max(ls))


##### 3.Nested Lists
if __name__ == '__main__':
    
    ls = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        ls.append([name, score])
    
    lowest2 = sorted(set(_[1] for _ in ls))[1]
    
    names=[]
    for i in ls:
        if i[1]==lowest2:
            names.append(i[0])
    names.sort()
            
    for i in names:
        print(i)       


##### 4.Finding the percentage
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    percentage = sum(student_marks[query_name]) / len(student_marks[query_name])
    print("%.2f" % percentage)


##### 5.Lists
if __name__ == '__main__':
    
    N = int(input())
    
    ls = []
    for _ in range(N):
        x = input()
        commands = x.strip().split(" ")
        command = commands[0]
        if command == "print":
            print(ls)
        elif command == "sort":
            ls.sort()
        elif command == "reverse":
            ls.reverse()
        elif command == "pop":
            ls.pop()
        elif command == "remove":
            ls.remove(int(commands[1]))
        elif command == "append":
            ls.append(int(commands[1]))
        elif command == "insert":
            i,j = int(commands[1]), int(commands[2])
            ls.insert(i, j)


##### 6.Tuples
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    h = hash(t)
    print(h)


###############################################################

##### Strings (https://www.hackerrank.com/domains/python/py-strings)

##### 1.sWAP cASE
def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
	
	
##### 2.String Split and Join
def split_and_join(line):
    # write your code here
    x = line.split()
    return "-".join(x)
        
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


##### 3.What's Your Name
def print_full_name(first, last):
    print("Hello "+first+" "+last+"! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
	

##### 4.Mutations
def mutate_string(string, position, character):
    s1 = string[:position]
    s2 = string[position+1:]
    return s1+character+s2

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
	
	
##### 5.Find a string
def count_substring(string, sub_string):
    n = 0
    for i in range(len(string)):
        if string[i:i+len(sub_string)] == sub_string:
            n +=1
        if i == len(string)- len(sub_string):
            break
    return n        

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
	
	
##### 6.String Validators
if __name__ == '__main__':
    s = input()
    a1,a2,a3,a4,a5 = False,False,False,False,False
    
    for i in s :
        if i.isalnum():
            a1 = True
        if i.isalpha():
            a2 = True
        if i.isdigit():
            a3 = True
        if i.islower():
            a4 = True
        if i.isupper():
            a5 = True
            
    print(a1);print(a2);print(a3);print(a4);print(a5)   


##### 7.Text Alignment
thickness = int(input())
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))


##### 8.Text Wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
	

##### 9.Designer Door Mat
n = input()
ls = n.split()
h, l = int(ls[0]), int(ls[1])

i = 0
while i < h // 2:
    mask = '.|.' * (i * 2 + 1)
    print(mask.center(l, '-'))
    i += 1


print('WELCOME'.center(l, '-'))

i = h // 2 - 1
while i >= 0:
    mask = '.|.' * (i * 2 + 1)
    print(mask.center(l, '-'))
    i -= 1

	
	
##### 10.String Formatting
def print_formatted(num):
    
    width = len("{0:b}".format(num))

    for i in range(1, num + 1):
        decimal = "{0:{width}d}".format(i, width=width)
        octal = "{0:{width}o}".format(i, width=width)
        hexadecimal = "{0:{width}X}".format(i, width=width)
        binary = "{0:{width}b}".format(i, width=width)

        print(f"{decimal} {octal} {hexadecimal} {binary}")


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
	
	
	
##### 11.Alphabet Rangoli
def print_rangoli(n):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    ls = []

    for i in range(n):
        substring = "-".join(alphabet[i:n])
        pattern_line = substring[::-1] + substring[1:]
        ls.append(pattern_line)

    max_width = len(ls[0])

    for i in range(n - 1, 0, -1):
        print(ls[i].center(max_width, '-'))

    for i in range(n):
        print(ls[i].center(max_width, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)



##### 12.Capitalize!
import math
import os
import random
import re
import sys

def solve(s):
    words = s.split(" ")
    out = ""
    for word in words :
        out += word.capitalize() + " "
    return out   
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()



##### 13.The Minion Game
def minion_game(string):
    # your code goes here
    vowels = ["A", "E", "I", "O", "U"]
    stuart, kevin = 0, 0
    for i in range(len(string)):
        if string[i] in vowels:
            kevin += len(string) - i
        else:
            stuart += len(string) - i
    if kevin > stuart :
        print("Kevin",kevin)
    elif stuart > kevin:
        print("Stuart",stuart)
    else:
        print("Draw")                



if __name__ == '__main__':
    s = input()
    minion_game(s)
	

#####################################################################

##### Sets (https://www.hackerrank.com/domains/python/py-sets)

##### 1.Introduction to Sets
def average(array):
    # your code goes here
    length = len(set(array))
    summ = sum(set(array))
    return summ/length

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
	

##### 2.No Idea!
n = input().split()
m = input().split()
a = set(input().split())
b = set(input().split())

count = 0

for value in m:
    count = count + 1 if value in a else count - 1 if value in b else count

print(count)


##### 3.Symmetric Difference
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


##### 4.Set .add()
n = int(input())

names = set()

for i in range(n):
    name = input()
    names.add(name)

print(len(names))



##### 5.Set .discard(), .remove() & .pop()
n = int(input())
s = set(map(int, input().split()))

for _ in range(int(input())):
    command, *args = input().split()
    getattr(s, command)(*map(int, args))

print(sum(s))



##### 6.Set .union() Operation
n = int(input())
a = set(map(int, input().strip().split(' ')))
m = int(input())
b = set(map(int, input().strip().split(' ')))
    
print(len(a.union(b)))



##### 7.Set .intersection() Operation
n = int(input())
a = set(map(int, input().strip().split(' ')))
m = int(input())
b = set(map(int, input().strip().split(' ')))    
print(len(a.intersection(b)))



##### 8.Set .difference() Operation
n = int(input())
a = set(map(int, input().strip().split(' ')))
m = int(input())
b = set(map(int, input().strip().split(' ')))
    
print(len(a.difference(b)))


##### 9.Set .symmetric_difference() Operation
n = int(input())
a = set(map(int, input().strip().split(' ')))
m = int(input())
b = set(map(int, input().strip().split(' ')))
    
print(len(a.symmetric_difference(b)))

##### 10.Set Mutations
n = int(input())
s = set(map(int, input().split()))
num_cmds = int(input())

for _ in range(num_cmds):
    cmd, *args = input().split()
    get_set = set(map(int, input().split()))
    if cmd == 'intersection_update':
        s.intersection_update(get_set)
    elif cmd == 'update':
        s.update(get_set)
    elif cmd == 'difference_update':
        s.difference_update(get_set)
    elif cmd == 'symmetric_difference_update':
        s.symmetric_difference_update(get_set)

print(sum(s))


##### 11.The Captain's Room
k = int(input())

room_number_ls = input().split()

# convert it to int list
for i in range(len(room_number_ls)):
    room_number_ls[i] = int(room_number_ls[i])

x = (sum(set(room_number_ls)) * k - sum(room_number_ls))    
captain_room_number = x // (k - 1)

print(captain_room_number)


##### 12.Check Subset
n = int(input())
for i in range(n):
    a = int(input())
    set_a = set(map(int, input().split()))
    b = int(input())
    set_b = set(map(int, input().split()))

    print("True" if len(set_a - set_b) == 0 else "False")


##### 13.Check Strict Superset
a = set(input().split())
c, v = 0, 0

n = int(input())
for i in range(n):
    input_data = set(input().split())
    if a.issuperset(input_data):
        c += 1
    else:
        v += 1
print('False' if v != 0 else 'True')


#########################################################################

##### Collections (https://www.hackerrank.com/domains/python/py-collections)

##### 1.collections.Counter()
from collections import Counter as c

x = int(input())
s = input().split()
s_ls = list(map(int, s))
n = int(input())
    
summ = 0
available = c(s_ls)

for i in range(n):
    xx = input().split()
    size = int(xx[0])
    price = int(xx[1])
        
    if available[size] > 0:
        summ += price
        available[size] -= 1
        
print(summ)


##### 2.DefaultDict Tutorial
from collections import defaultdict

inp = input().split()
n = int(inp[0])
m = int(inp[1])
d = defaultdict(list)

for i in range(1, n + 1):
    s = input()
    d[s].append(str(i))

for i in range(m):
    query = input()
    result = d.get(query, ['-1'])
    print(' '.join(result) if result != ['-1'] else -1)


##### 3.Collections.namedtuple()
from collections import namedtuple

n = int(input())  # Number of students

s = input().split()
S = namedtuple('Student', s) 

students = []

for i in range(n):
    s_data = input().split()
    student_obj = S(*s_data) 
    students.append(student_obj)

total = 0
for s in students:
    total += int(s.MARKS)

avg = total / n

print("{:.2f}".format(avg))


##### 4.Collections.OrderedDict()
from collections import OrderedDict

od = OrderedDict()
n = int(input())

for _ in range(n):
    in_data = input().rsplit(' ', 1)
    item = in_data[0]
    price = int(in_data[1])

    od[item] = od.get(item, 0) + price

for item, total_price in od.items():
    print(item, total_price)



##### 5.Word Order
from collections import Counter

n = int(input())
ls = []

for i in range(n):
    x = input()
    ls.append(x)

total = Counter(ls)
l = len(total)

print(l)
print(*total.values())


##### 6.Collections.deque()
from collections import deque

d = deque()

cmds = ['append', 'pop', 'popleft', 'appendleft']

n = int(input())
for _ in range(n):
    x = input().split()
    cmd = x[0]
    if cmd == cmds[0]:
        d.append(int(x[1]))
    elif cmd == cmds[1]:
        d.pop()
    elif cmd == cmds[2]:
        d.popleft()
    elif cmd == cmds[3]:
        d.appendleft(int(x[1]))

print(*d)


##### 7.Piling Up!
from collections import deque

num = int(input())
for i in range(num):
    inp1 = input()
    inp2 = input().split()
    inp2 = deque(map(int, inp2))
    
    flag = 1
    l = len(inp2)
    

    for j in range(l- 1):
        if inp2[0] >= inp2[1]:
            inp2.popleft()
        elif inp2[-1] >= inp2[-2]:
            inp2.pop()
        else:
            flag = 0
            break

    if flag ==1:
        print("Yes")
    else:
        print("No")



#############################################################################

##### Date and Time (https://www.hackerrank.com/domains/python/py-date-time)

##### 1.Calendar Module
import datetime
import calendar

#month, day, year
in_date = input().split()

#and it should be year,month,day
our_date = datetime.date(int(in_date[2]), int(in_date[0]), int(in_date[1]))
result = calendar.day_name[our_date.weekday()].upper()
print(result)


##### 2.Time Delta
import math
import os
import random
import re
import sys
import datetime

# Complete the time_delta function below.
def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    t1_out = datetime.datetime.strptime(t1, format)
    t2_out = datetime.datetime.strptime(t2, format)
    delta = t1_out - t2_out
    return delta
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)
        delta = delta.total_seconds()
        if delta<0:
            delta = delta * (-1)    
        delta = int(delta)
        fptr.write(str(delta) + '\n')

    fptr.close()


#####################################################################

##### Exceptions (https://www.hackerrank.com/challenges/exceptions)

##### 1.Exceptions
for _ in range(int(input())):
    a1, a2 = input().split()
    try:
        print(int(a1) // int(a2))
    except Exception as e:
        print("Error Code:", e)

######################################################################

##### Built-ins 

##### 1.Zipped!  (https://www.hackerrank.com/challenges/zipped)
inp = input()
inp = inp.split()
n, x = int(inp[0]), int(inp[1])
scores = []
for i in range(x):
    scores.append(list(map(float, input().split())))
for i in zip(*scores):
    print(sum(i) / len(i))


##### 2.Athlete Sort (https://www.hackerrank.com/challenges/python-sort-sort)
import math
import os
import random
import re
import sys

if __name__ == '__main__':

    nm = input().split()
    n,m = int(nm[0]), int(nm[1])
    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    for i in sorted(arr, key=lambda x: x[k]):
        print(*i)



##### 3.ginortS (https://www.hackerrank.com/challenges/ginorts)
n = input()
digits_odd= []
digits_even = []
uppers = []
lowers = []
for i in n:
    if i.isdigit():
        if int(i)%2 == 0:
            digits_even.append(int(i))
        else:
            digits_odd.append(int(i))    
    elif i.isupper():
        uppers.append(i)
    else:
        lowers.append(i)
                
digits_odd.sort()
digits_even.sort()
uppers.sort()
lowers.sort() 

out1 = "".join(lowers)
out2 = "".join(uppers)
out3 = "".join(str(i) for i in digits_odd)
out4 = "".join(str(i) for i in digits_even)

print(out1+out2+out3+out4)

###############################################################################

##### Python Functionals (https://www.hackerrank.com/challenges/map-and-lambda-expression)

##### 1.Map and Lambda Function
cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    ls = [0, 1]
    if n < 2:
        return ls[:n]
    for i in range(2, n):
        ls.append(ls[i - 1] + ls[i - 2])
    return ls

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
	
################################################################################

##### Regex and Parsing challenges (https://www.hackerrank.com/domains/python/py-regex)

##### 1.Detect Floating Point Number
import re

T = int(input())
for _ in range(T):
    inp = input()
    print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', inp)))

##### 2.Re.split()
regex_pattern = r"[,.]"	# Do not delete 'r'.

import re
print("\n".join(re.split(regex_pattern, input())))


##### 3.Group(), Groups() & Groupdict()
import re

def find_repeating_character(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1] and s[i].isalnum():
            return s[i]
    return -1

input_str = input()
result = find_repeating_character(input_str)
print(result)

##### 4.Re.findall() & Re.finditer()
import re

c = 'QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm'
v = 'AEIOUaeiou'

if __name__ == "__main__":
    
    inp = input()
    
    res = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), inp)
    res = "\n".join(res or ['-1'])
    print(res)

##### 5.Re.start() & Re.end()
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


##### 6.Regex Substitution
import re

n = int(input())

for _ in range(n):
    line = input()
    modified_line = re.sub(r'(?<= )(&&|\|\|)(?= )', lambda match: "and" if match.group(0) == "&&" else "or", line)
    print(modified_line)


##### 7.Validating Roman Numerals
regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))


##### 8.Validating phone numbers
import re

for _ in range(int(input())):
    number = input()
    p = '^[789][0-9]{9}$'
    print("YES" if bool(re.match(p, number)) else "NO")


##### 9.Validating and Parsing Email Addresses
import re

for _ in range(int(input())):
    inp = input().split()
    name, email = inp[0], inp[1]
    
    if re.match(r'<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>', email):
        print(name,email)


##### 10.Hex Color Code
import re

for _ in range(int(input())):
    pattern = r"(#[0-9A-Fa-f]{3}|#[0-9A-Fa-f]{6})(?:[;,.)]{1})"
    res = re.findall(pattern, input())
    for r in res:
        print(r)


##### 11.Validating UID
import re

for _ in range(int(input())):
    uid = input()
    if re.match(r'^(?!.*(.).*\1)(?=(?:.*[A-Z]){2})(?=(?:.*\d){3})(?=[a-zA-Z0-9]{10}$)', uid):
        print("Valid")
    else:
        print("Invalid")


##### 12.Validating Credit Card Numbers
import re

for _ in range(int(input())):
    num = "".join(input())
    if re.match(r'^[456][\d]{3}-?[\d]{4}-?[\d]{4}-?[\d]{4}$', num) and not re.search(r'(\d)\1{3,}', num.replace("-", "")):
        print("Valid")
    else:
        print("Invalid")


##### 13.Validating Postal Codes
regex_integer_in_range = r"^[1-9][\d]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	# Do not delete 'r'.

import re

num = input()
regex_integer_in_range = r'^[1-9][\d]{5}$'
matches = re.findall(regex_alternating_repetitive_digit_pair, num)
is_valid = bool(re.match(regex_integer_in_range, num) and len(matches) < 2)
print(is_valid)

import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)


#################################################################################

##### XML (https://www.hackerrank.com/domains/python/xml)

##### 1.XML 1 - Find the Score
import sys
import xml.etree.ElementTree as etree

def get_attr_number(node):
    # your code goes here
    count = len(node.attrib)
    for child in node:
        count += get_attr_number(child)
    return count


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))
	
	
##### 2.XML2 - Find the Maximum Depth
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    level = level if level != -1 else 0
    maxdepth = level if level > maxdepth else maxdepth
    for e in elem:
        depth(e, level+1)

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
	
	
#####################################################################

##### Closures and Decorations (https://www.hackerrank.com/domains/python/closures-and-decorators)

##### 1.Standardize Mobile Number Using Decorators
def wrapper(f):
    def fun(l):
        out = []
        for t in l:
            b = t[-10:]
            res = '+91 {} {}'.format(b[:5], b[5:])
            out.append(res)
        f(out)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 



##### 2.Decorators 2 - Name Directory
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        ls = sorted(people, key = lambda x: (int(x[2])))
        return [ f(p) for p in ls]
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
	
#######################################################################################

##### Numpy (https://www.hackerrank.com/domains/python/numpy)

##### 1.Arrays
import numpy

def arrays(arr):
    # complete this function
    # use numpy.array
    res = numpy.array(arr[::-1], float)
    return res

arr = input().strip().split(' ')
result = arrays(arr)
print(result)


##### 2.Shape and Reshape
import numpy

arr = input().split()
arr = list(map(int, arr))
arr = numpy.array(arr)
res = arr.reshape(3, 3)
print(res)


##### 3.Transpose and Flatten
import numpy

inp = input().split()
n = int(inp[0])
m = int(inp[1])

array = []
for i in range(n):
    inp = input().split()
    row = list(map(int, inp))
    array.append(row)

array = numpy.array(array)

print(array.T)
print(array.flatten())


##### 4.Concatenate
import numpy

n, m, p = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(m)]

print(numpy.concatenate((arr1, arr2)))


##### 5.Zeros and Ones
import numpy

inp = input()
inp = inp.split()
d = [int(x) for x in inp]

print(numpy.zeros(tuple(d), dtype=int))
print(numpy.ones(tuple(d), dtype=int))


##### 6.Eye and Identity
import numpy
numpy.set_printoptions(legacy='1.13')

inp = input().split()
n = int(inp[0])
m = int(inp[1])
print(numpy.eye(n, m,dtype=float))


##### 7.Array Mathematics
import numpy

inp = input().split()
n = int(inp[0])
m = int(inp[1])

a = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    a.append(row)
a = numpy.array(a)
  
b = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    b.append(row)
b = numpy.array(b)
        

print(a + b); print(a - b); print(a * b); print(a // b); print(a % b); print(a**b)



##### 8.Floor, Ceil and Rint
import numpy
numpy.set_printoptions(legacy="1.13")

inp = input().split()

arr = numpy.array(inp,dtype=float)

print(numpy.floor(arr))
print(numpy.ceil(arr))
print(numpy.rint(arr))


##### 9.Sum and Prod
import numpy

inp = input().split()
n = int(inp[0])
m = int(inp[1])

arr = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    arr.append(row)

arr = numpy.array(arr)
print(numpy.prod(numpy.sum(arr, axis=0)))



##### 10.Min and Max
import numpy

inp = input().split()
n = int(inp[0])
m = int(inp[1])

arr = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    arr.append(row)

arr = numpy.array(arr)
print(numpy.max(numpy.min(arr, axis = 1)))




##### 11.Mean, Var, and Std
import numpy

inp = input().split()
n = int(inp[0])
m = int(inp[1])

arr = []
for _ in range(n):
    row = [int(x) for x in input().split()]
    arr.append(row)

arr = numpy.array(arr, dtype = float)

print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))
print(round(numpy.std(arr, axis = None), 11))



##### 12.Dot and Cross
import numpy as np



n = int(input())
arr1 = []
for _ in range(n):
    row = list(map(int, input().strip().split()))
    arr1.append(row)

arr1 = np.array(arr1)

arr2 = []
for _ in range(n):
    row = list(map(int, input().split()))
    arr2.append(row)

arr2 = np.array(arr2)

print(np.dot(arr1, arr2))


##### 13.Inner and Outer
import numpy

arr1 = numpy.array(list(map(int, input().split())))
arr2 = numpy.array(list(map(int, input().split())))

print(numpy.inner(arr1, arr2))
print(numpy.outer(arr1, arr2))


##### 14.Polynomials
import numpy

coefficients = input()
coefficients_ls = list(map(float, coefficients.split()))

x = float(input())

result = numpy.polyval(coefficients_ls, x)

print(result)


##### 15.Linear Algebra
import numpy

n = int(input())

arr = []
for _ in range(n):
    inp = input()
    inp = [float(x) for x in inp.split()]
    arr.append(inp)

arr = numpy.array(arr, dtype=float)
print(round(numpy.linalg.det(arr), 2))


################################################################################