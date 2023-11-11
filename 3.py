from random import randint
from resource import *
from time import perf_counter

timeStart = perf_counter()


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


def Scarecrow_sort(lst, k):
    for i in range(k):
        if i + k < len(lst):
            lst[i::k] = Quick_sort(lst[i::k], 0, len(lst[i::k]) - 1)
    return lst

fin = open('input.txt', 'r')
(n, k), lst = map(int, fin.readline().split()), [int(x) for x in fin.readline().split()]
fin.close()
lst = Scarecrow_sort(lst, k)

fout = open('output.txt', 'w')
fout.write(("НЕТ", "ДА")[Sort_check(lst)])
fout.close()

print(f'Time: {perf_counter() - timeStart} seconds')
memoryUsage = getrusage(RUSAGE_SELF).ru_maxrss
memoryAns = int(format(memoryUsage)) / 1024
print(f'Memory: {str(memoryAns)} Kbits')
