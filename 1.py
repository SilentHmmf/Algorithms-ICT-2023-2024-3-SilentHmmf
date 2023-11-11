from random import randint
from resource import *
from time import perf_counter

timeStart = perf_counter()


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


print(f'Time: {perf_counter() - timeStart} seconds')
memoryUsage = getrusage(RUSAGE_SELF).ru_maxrss
memoryAns = int(format(memoryUsage)) / 1024
print(f'Memory: {str(memoryAns)} Kbits')
