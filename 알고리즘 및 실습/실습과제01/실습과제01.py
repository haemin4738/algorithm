def gcd_v1(a, b):
    alist = []
    blist = []
    for i in range(1, a):
        if a % i == 0:
            alist.append(i)
    for i in range (1, b):
        if b % i ==0:
            blist.append(i)
    print(a, "의 약수 = ", alist)
    print(b, "의 약수 =  ", blist)

    for i in range(len(alist) - 1, 0, -1):
        if alist[i] in blist:
            return alist[i]

    return 1
def gcd_v2(a, b):
    alist = []
    for i in range(1, a):
        if a % i == 0:
            alist.append(i)
    print(a, "의 약수 = ", alist)
    for i in range(len(alist) - 1, 0, -1):
        if b % alist[i] == 0:
            return alist[i]

    return 1
def gcd_v3(a, b):
    print("gcd_v3", (a,b))
    while b != 0:
        a, b = b, a % b 
    return a

def gcd_v4(a, b):
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b /gcd_v4(a, b)


print("60과 28의 최대 공약수 = ", gcd_v1(60,28))
print("60과 28의 최대 공약수 = ", gcd_v2(60,28))
print("60과 28의 최대 공약수 = ", gcd_v4(60,28))
print("60과 28의 최소 공배수 = ", lcm(60,28))