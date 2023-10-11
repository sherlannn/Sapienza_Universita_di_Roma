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
