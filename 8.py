from random import randint
from math import sqrt
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
n, k = (int(x) for x in fin.readline().split())
lst = [list(map(int, fin.readline().split())) for _ in range(n)]

lst = [(sqrt(x[0]**2 + x[1]**2), x) for x in lst] # [(sqrt(x1**2 + y1**2), (x1, y1)), ...]
Quick_sort(lst, 0, len(lst) - 1)

ans = [str(lst[i][1]) for i in range(k)]
fout = open('output.txt', 'w')
fout.write(','.join(ans))
fout.close()
