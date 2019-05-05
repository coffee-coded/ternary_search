x = int(input())


def fun(x):
    return (2*x*x) - (12*x)+(7)

def ts(l, r):
    for i in range(200):
        l1 = l+(r-l)/3
        l2 = l + 2*(r-l)/3
        if fun(l1)<fun(l2):
            r = l2
        else:
            l = l1
    return(round(fun(r)))

for i in range(x):
    inp = input().split(" ")
    inp = [int(x) for x in inp]
    l = inp[0]
    r = inp[1]
    print((ts(l,r)))