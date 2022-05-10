def isr(a):  
    "......"  
    f=0  
    if (a%400 == 0):    
        f=1  
    elif (a%4 == 0):    
        if (a%100 == 0):    
            f=0  
        else:    
            f=1  
    else:    
        f=0  
    return f

lm = [31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
s = raw_input()
q = s.split(" ")
y, m = int(q[0]), int(q[1])
if (m == 2):
    if (isr(y) == 1):
        print("29")
    else:
        print("28")
else:
    print(lm[m - 1])
