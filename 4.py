from random import randint
from resource import *
from time import perf_counter

timeStart = perf_counter()


def Occurence_counter(dots, section):
    pass


def Sort_check(lst):
    """
    >>> Sort_check([1,2,3,4,4])
    True
    >>> Sort_check([1,2,2,1])
    False
    """
    return all(lst[i] <= lst[i+1] for i in range(len(lst) - 1))

def Partition(lst, left, right):
    """
    >>> lst = [3, 4, 2, 5, 1]
    >>> Partition(lst, 0, 4)
    2
    >>> lst
    [1, 2, 3, 5, 4]
    """
    key, j = lst[left], left

    for i in range(left + 1, right + 1):
        if lst[i] < key:
            j += 1
            lst[j], lst[i] = lst[i], lst[j]

    lst[left], lst[j] = lst[j], lst[left]
    return j


def Quick_sort(lst, left, right):
    """
    >>> lst = [3, 4, 2, 5, 1]
    >>> Quick_sort(lst, 0, len(lst) - 1)
    [1, 2, 3, 4, 5]

    >>> lst = [7,6,5,4,3,2,1]
    >>> Quick_sort(lst, 0, len(lst) - 1)
    [1, 2, 3, 4, 5, 6, 7]
    """
    if left < right:
        key = randint(left, right)
        lst[left], lst[key] = lst[key], lst[left]

        mid = Partition(lst, left, right)

        Quick_sort(lst, left, mid)
        Quick_sort(lst, mid + 1, right)

    return lst


fin = open('input.txt')
s, p = map(int, fin.readline().split())
sectionList = [[int(x) for x in fin.readline().split()] for _ in range(s)]
dotList = list(map(int, fin.readline().split()))
fin.close()

sumList = [0] * p
sectionList = Quick_sort(sectionList, 0, len(sectionList) - 1)

for i, dot in enumerate(dotList):
    j = 0
    while sectionList[j][0] <= dot:
        if sectionList[j][1] >= dot:
            sumList[i] += 1
        j += 1
        if j >= len(sectionList):
            break

fout = open('output.txt', 'w')
fout.write(' '.join([str(x) for x in sumList]))
fout.close()

print(f'Time: {perf_counter() - timeStart} seconds')
memoryUsage = getrusage(RUSAGE_SELF).ru_maxrss
memoryAns = int(format(memoryUsage)) / 1024
print(f'Memory: {str(memoryAns)} Kbits')