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
