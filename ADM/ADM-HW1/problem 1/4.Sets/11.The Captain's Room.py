# Enter your code here. Read input from STDIN. Print output to STDOUT

k = int(input())

room_number_ls = input().split()

# convert it to int list
for i in range(len(room_number_ls)):
    room_number_ls[i] = int(room_number_ls[i])

x = (sum(set(room_number_ls)) * k - sum(room_number_ls))    
captain_room_number = x // (k - 1)

print(captain_room_number)
