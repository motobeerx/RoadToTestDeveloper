import os
import random


def randomeTestCases():
    while True:
        try:
            print(r"Insert file's path (for example C:/User/Documents/test.txt): ", end='')
            path = input()
            print(r"Insert file numbers: ", end='')
            n = int(input())
            line_list = []
            random_cases_number = [0]
            if not os.path.exists(path):
                raise FileExistsError

            with open(path) as f:
                f_content = f.readline()
                while f_content != '':
                    line_list.append(f_content)
                    f_content = f.readline()
            f.close()

            i = 2
            random_cases_number.append(random.randint(1, len(line_list) - 1))  # think it is not nesesary and i =1

            while i < n + 1:
                random_cases_number.append(random.randint(1, len(line_list) - 1))
                if random_cases_number[i] in random_cases_number[:i]:
                    random_cases_number.pop()
                    i -= 1
                i += 1

            res_path = os.path.split(path)
            res_path = os.path.join(res_path[0] + r'\res_' + res_path[1])

            with open(res_path, 'w') as f:
                for x in random_cases_number:
                    f.write(line_list[x])
            f.close()
        except FileExistsError:
            print('\nThe given path "' + path + '" does not exist.')
            print('Would you like to try one more time? Y/N: ', end='')
            contin = input()
            if contin == 'N' or contin == 'n':
                return

#/home/anton/Downloads/1.txt
randomeTestCases()
