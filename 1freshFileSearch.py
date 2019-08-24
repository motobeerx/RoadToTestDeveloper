import os
from datetime import datetime


def freashFileSearch():
    while True:
        try:
            print(r"Enter folder's path (for example C:/User/Documents): ", end='')
            path = input()
            print(r"Enter file extension (for example .txt): ", end='')
            ext = input()
            if not os.path.isdir(path):
                raise FileExistsError
            files = os.listdir(path)
            if ext[0] != '.':
                ext = '.' + ext
            files = [[os.path.join(path, files[i]), os.path.getctime(os.path.join(path, files[i]))] for i in range(len(files)) if ext == os.path.splitext(files[i])[1]]
            assert len(files) != 0
            d = max(x[1] for x in files)
            files = [[files[i][0], str(datetime.fromtimestamp(int(files[i][1])))] for i in range(len(files)) if d - files[i][1] <= 10]
            files.sort(key=lambda item: item[1], reverse=True)
            for i in range(len(files)):
                print(files[i][0] + '  ||  ' + files[i][1])
            return
        except FileExistsError:
            print('\nThe given directory "' + path + '" does not exist.')
            print('Would you like to try one more time? Y/N: ', end='')
            cont_descis = input()
            if cont_descis == 'N' or cont_descis == 'n':
                return
        except AssertionError:
            print('\nNo " *' + ext + ' " file has been found in the "' + path + '"')
            print('Would you like to try one more time ? Y/N: ', end='')
            cont_descis = input()
            if cont_descis == 'N' or cont_descis == 'n':
                return


freashFileSearch()
