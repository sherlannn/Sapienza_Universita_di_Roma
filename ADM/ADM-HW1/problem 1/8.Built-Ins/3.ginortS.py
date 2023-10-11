# Enter your code here. Read input from STDIN. Print output to STDOUT

# what the fuck is this piece of shit :/

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
