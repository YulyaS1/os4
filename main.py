import time
def fnc(n):
    b = 3
    c = 3
    s = 0
    for j in range(1,n+1):
        a = 0
        for i in range(1,100000001):
            a += b*2 + c - j
        s+=a
    print(s)
    return s
start = time.time()
fnc(2)
end = time.time()
print(end-start)