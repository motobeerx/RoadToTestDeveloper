import os
from datetime import datetime


def merge(A:list, B:list, key:int):
    C = []
    i=k=0
    while i < len(A) and k < len(B):
        if A[i][key] >= B[k][key]:
            C.append(A[i])
            i += 1
        else:
            C.append(B[k])
            k += 1
    while i < len(A):
        C.append(A[i])
        i += 1
    while k < len(B):
        C.append(B[k])
        k += 1
    return C


def mergeSort(A, key:int):
    if len(A) <= 1:
        return
    mid = len(A)//2
    L = [A[i] for i in range(0, mid)]
    R = [A[i] for i in range(mid, len(A))]
    mergeSort(L, key)
    mergeSort(R, key)
    C = merge(L, R, key)
    for i in range(len(A)):
        A[i] = C[i]


def freashFileSearch(path: str, ext: str = '.txt'):
    if not os.path.isdir(path) :
        print('The given directory "' + path + '" does not exist.')
        return
    if ext[0] != '.':
        ext = '.'+ext
    files = os.listdir(path)
    i=0
    while i < len(files):
        if ext != os.path.splitext(files[i])[1]:
            files.pop(i)
            i -= 1
        else:
            files[i] = [os.path.join(path, files[i]), os.path.getctime(os.path.join(path, files[i]))]
        i += 1
    if len(files) == 0:
        print('No *.'+ext+' file has been found in the "'+path+'"')
        return
    mergeSort(files, 1)
    d = files[0][1]
    i = 0
    while i < len(files):
        if d - files[i][1] > 10:
            files.pop(i)
            i -= 1
        else:
            files[i][1] = str(datetime.fromtimestamp(int(files[i][1])))
        i += 1
    for i in range(len(files)):
        print(files[i][0]+'  ||  '+files[i][1])


print(r"Insert folder's path (for example C:/User/Documents): ", end='')
path = input()
print(r"Enter files' extension (for example .txt): ", end='')
extension = input()
freashFileSearch(path, extension)
