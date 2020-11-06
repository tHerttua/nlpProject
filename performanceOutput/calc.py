x = [0.391 , 1.146 , 0.036 , 0.131]
y= [0.33 , 1.598 , 0.034 , 0.13]
z = [0.328 , 1.277 , 0.034 , 0.135]
c = [0.308 , 1.413 , 0.035 , 0.133]


def sumlist(alist):
    tot = 0
    for num in alist:
        tot += num
    return tot

print(
(
sumlist(y)+sumlist(z)+sumlist(x)+sumlist(c)
)/4
)

print(
    (y[1] +z[1]+c[1]+x[1])/4
)

print(sumlist(y))