ml = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isleap(a):    
    if (a%400 == 0): return True    
    elif (a%4 == 0):      
        if (a%100 == 0): return False  
        else: return True  
    else: return False 

def day(y, m, d):
    if (isleap(y)): ml[1] = 29
    c = 0
    for mf in range(0, m):
        for df in range(1, ml[mf]+1):
            c += 1
            if (mf == m - 1 and df == d): break
    return c

y,m1,d1,m2,d2=map(int,raw_input().split())
print day(y,m2,d2)-day(y,m1,d1)  
