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
