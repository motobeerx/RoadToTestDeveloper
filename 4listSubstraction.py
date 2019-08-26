import collections
a, b = ["Anton","Alex", "Dima",'Anton', "Kate", "Galina", "Ivan",'Marie','Denis', 'Anton',"Dima", "Doma", 'dsa', 'Galina', 'Kate', 'Kate', 'Kate', 'Anton','Anton'],\
       ['Alex', 'Alex', "Dima", "Ivan", "Kate",'Anton']
print('\nOriginal List:', *a, '\n')
print('Substracted List:', *b, '\n\nResult: ', sep=' ', end='')
a_count = collections.Counter(a)
b_count = collections.Counter(b)
c_count = a_count.copy()
for x in a_count:
    if x in b_count:
        del c_count[x]
c = []
for x in c_count:
    for j in range(c_count[x]):
        c.append(x)
print(*c,'\n')
