#merge sort with a insert sort for a small amounts of numbers which usually is faster. Enjoy :D

def insert_sort(v, l, r):
    for i in range(l + 1, r + 1):
        ind = i - 1
        x = v[i]
        while(ind >= l and x < v[ind]):
            v[ind + 1] = v[ind]
            ind -=1
        v[ind + 1] = x
#end def
def merge(v, p1, k1, p2, k2, t):
    l = p1
    r = k2
    ind_t = 0
    while(p1 <= k1 and p2 <= k2):
        a = v[p1]
        b = v[p2]
        if(a <= b):
            t[ind_t] = a
            ind_t += 1
            p1+=1
        else:
            t[ind_t] = b
            ind_t += 1
            p2+=1
    while(p1 <= k1):
        a = v[p1]
        t[ind_t] = a
        ind_t += 1
        p1+=1
    while(p2 <= k2):
        b = v[p2]
        t[ind_t] = b
        ind_t += 1
        p2+=1
    for i in range(ind_t): v[i + l] = t[i]
#end def
def merge_sort(v, l, r, t):
    if(r - l >= 1):
        if(r - l <= 32):
            insert_sort(v, l, r)
            return
        s = (l + r)//2
        merge_sort(v, l, s, t)
        merge_sort(v, s + 1, r, t)
        if v[s] <= v[s+1]: return
        merge(v, l, s, s+1, r, t)
#end def
def sort(v):
    n = len(v)
    t = [None] * n
    merge_sort(v, 0, n - 1, t)
#end def

T = [int(x) for x in input().split()]
sort(T)
print(T)