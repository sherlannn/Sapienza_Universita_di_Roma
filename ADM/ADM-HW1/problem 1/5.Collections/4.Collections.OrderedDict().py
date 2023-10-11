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
