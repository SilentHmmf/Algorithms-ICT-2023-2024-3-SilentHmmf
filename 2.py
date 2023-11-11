
def Merge(lst, l, q ,r):

    L = lst[l:q] + [float('inf')]
    R = lst[q:r] + [float('inf')]
    for i in range(l, r):
        if L[0] <= R[0]:
            lst[i] = L.pop(0)
        else:
            lst[i] = R.pop(0)


def MergeSort(lst, l, r):
    if l < r-1:
        q = (l + r) // 2
        MergeSort(lst, l, q)
        MergeSort(lst, q, r)
        Merge(lst, l, q, r)

# def IsSorted(lst):
#     if lst == sorted(lst):
#         return True
#     return False


fin = open('input.txt')
n = fin.readline()
lst = list(map(int, fin.readline().split()))
#lst = [x + 10**9 for x in range(10**5, -1, -1)]
#lst = [x + 10**9 for x in range(10**5)]

fin.close()

MergeSort(lst, 0, len(lst))

fout = open('output.txt', 'w')
fout.write(' '.join(list(map(str, lst))))
fout.close()

print(f'Time: {perf_counter() - timeStart} seconds')
memoryUsage = getrusage(RUSAGE_SELF).ru_maxrss
memoryAns = int(format(memoryUsage))/1024
print(f'Memory: {str(memoryAns)} Kbits')