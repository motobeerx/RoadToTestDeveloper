import collections
a, b =  ["Anton","Alex", "Dima",'Anton', "Kate", "Galina", "Ivan",'Marie','Denis', 'Anton',"Dima", "Doma", 'dsa', 'Galina', 'Kate', 'Kate', 'Kate', 'Anton','Anton'], ["Dima", "Ivan", "Kate",'Anton']
print('\nOriginal List:', *a, '\n')
print('Substracted List:', *b, '\n\nResult: ', sep=' ', end='')
d= collections.deque(a)
[print(d[i], end=' ') for i in range(len(d)) if d[i] not in b]
print('\n')
