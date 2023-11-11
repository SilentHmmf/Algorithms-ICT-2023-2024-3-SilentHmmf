from random import randint
from resource import *
from time import perf_counter

timeStart = perf_counter()


def Sort_check(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))

def Partition(lst, left, right):
    key, j = lst[left], left

    for i in range(left + 1, right + 1):
        if lst[i] < key:
            j += 1
            lst[j], lst[i] = lst[i], lst[j]

    lst[left], lst[j] = lst[j], lst[left]
    return j


def Quick_sort(lst, left, right):
    if left < right:
        key = randint(left, right)
        lst[left], lst[key] = lst[key], lst[left]

        mid = Partition(lst, left, right)

        Quick_sort(lst, left, mid)
        Quick_sort(lst, mid + 1, right)

    return lst


fin = open('input.txt')
n, m, k = map(int, fin.readline().split())
lst = [fin.readline().strip() for _ in range(n)]
fin.close()
lst = [''.join([lst[i][j] for i in range(n)]) for j in range(m)]
lst = [(s, i+1) for i, s in enumerate(lst)]

for _ in range(k):
    lst = Quick_sort(lst, 0 , len(lst) - 1)
    lst = [(s[1:] + s[0], i) for s, i in lst]

fout = open('output.txt', 'w')
fout.write(' '.join(list(map(str, [a[1] for a in lst]))))
fout.close()

print(f'Time: {perf_counter() - timeStart} seconds')
memoryUsage = getrusage(RUSAGE_SELF).ru_maxrss
memoryAns = int(format(memoryUsage)) / 1024
print(f'Memory: {str(memoryAns)} Kbits')
