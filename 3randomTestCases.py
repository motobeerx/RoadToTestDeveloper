import os
import random


def randomeTestCases():
    while True:
        try:
            print(r"Insert file's path (for example C:/User/Documents/test.txt): ", end='')
            path = input()
            print(r"Insert number of test cases: ", end='')
            n = int(input())
            line_list = []
            random_cases_number = [0]
            assert os.path.exists(path)
            assert os.path.splitext(path)[1] == '.txt'
            with open(path, 'r') as f:
                f_content = f.readline()
                while f_content != '':
                    line_list.append(f_content)
                    f_content = f.readline()
                assert n <= len(line_list)
                i = 1
                while i < n + 1:
                    random_cases_number.append(random.randint(1, len(line_list) - 1))
                    if random_cases_number[i] in random_cases_number[:i]:
                        random_cases_number.pop()
                        i -= 1
                    i += 1
            with open(path, 'w') as f:
                [f.write(line_list[i]) for i in range(len(line_list)) if i not in random_cases_number[1:]]
            res_path = os.path.split(path)
            res_path = os.path.join(res_path[0] + r'\res_' + res_path[1])
            with open(res_path, 'w') as f:
                [f.write(line_list[x]) for x in random_cases_number]
            return res_path
        except AssertionError:
            if not os.path.exists(path):
                print('\nThe given path "' + path + '" does not exist.')
            elif  os.path.splitext(path)[1] != '.txt':
                print(f'The given file extension is {os.path.splitext(path)[1]}, but should be .txt!')
            elif n > len(line_list):
                print(f'Opps.. The inserted number of test cases bigger than current number in the file - {len(line_list)}')
            print('Would you like to try one more time? Y/N: ', end='')
            contin = input()
            if contin == 'N' or contin == 'n':
                return
        except ValueError:
            print("Test cases number must be integer type !")
            print('Would you like to try one more time? Y/N: ', end='')
            contin = input()
            if contin == 'N' or contin == 'n':
                return


print(randomeTestCases())
