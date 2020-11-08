#parser
r = [0.250 , 0.579 , 0.004 , 0.012]
t= [0.252 , 0.66 , 0.004 , 0.012]
n = [0.252 , 0.467 , 0.004 , 0.013]
s = [0.255 , 0.435, 0.04 , 0.012]
o = [0.252, 0.480, 0.004, 0.012]

#rouge
rr = [0.033 , 0.558 , 1.121 ]
rt = [0.036 , 0.651 , 1.306 ]
rn = [0.034 , 0.587 , 1.179 ]
rs = [0.033 , 0.609 , 1.223 ]
ro = [0.033 , 0.637 , 1.28 ]

#summarizer

def sumlist(alist):
    tot = 0
    for num in alist:
        tot += num
    return tot

print("IR")
print(
(
sumlist(o)+sumlist(s)+sumlist(n)+sumlist(t)+sumlist(r)
)/5
)

print(
    (o[1] +s[1]+n[1]+t[1]+r[1])/5
)

print("ROUGE")
print(
(
sumlist(ro)+sumlist(rs)+sumlist(rn)+sumlist(rt)+sumlist(rr)
)/5
)
print(
    (ro[1] +rs[1]+rn[1]+rt[1]+rr[1])/5
)
print(sumlist(ro),sumlist(rs),sumlist(rn),sumlist(rt),sumlist(rr))