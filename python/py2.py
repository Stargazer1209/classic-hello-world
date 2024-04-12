def isa(s):
    if (s[0] == s[3] and s[1] == s[2] and s[0] == s[1]):
        return True
    else:
        return False
s = raw_input()
t = s.split(" ")
t = sorted(t)
print(t)
a = 0
f = -1
m = "10000"
for i in range(0, len(t)):
    if (t[i] < m):
        m = t[i]
        f = i
        if (isa(t[i])):
            a = 1
if (a == 0):
    print ()
