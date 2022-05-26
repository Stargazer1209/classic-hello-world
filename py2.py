def kaisa(s):  
    if 'a'<=s<'x' or 'A'<=s<'X':  
        ms=chr(ord(s)+3)  
    elif 'x'<=s<='z' or 'X'<=s<='Z':  
        ms=chr(ord(s)-23)  
    return ms  

s = raw_input()
l = ""
for i in range(0, len(s)):
    if s[i].isalpha():
        l += kaisa(s[i])
    else:
        l += s[i]
print(l)
