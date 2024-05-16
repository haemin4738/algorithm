import random
import time


def algorithmA(a) :
    n = len(a)
    for i in range(n - 1) :
        for j in range(i + 1, n) :
            if a[i] == a[j] :
                return True
    return False

def algorithmB(a) :
    n = len(a)
    a.sort()
    for i in range(n - 1) :
        if a[i] == a[i + 1] :
            return True
    return False

my_list = []
for i in range(0, 100) :
    my_list.append(random.randint(1, 10000))

start = time.time()
for i in range(100000) :
    algorithmA(my_list)
end = time.time()
print(end - start, algorithmA(my_list))



start = time.time()
for i in range(100000) :
    algorithmB(my_list)
end = time.time()
print(end - start, algorithmB(my_list))

