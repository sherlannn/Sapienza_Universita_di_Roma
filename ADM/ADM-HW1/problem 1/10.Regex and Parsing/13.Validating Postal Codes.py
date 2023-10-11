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