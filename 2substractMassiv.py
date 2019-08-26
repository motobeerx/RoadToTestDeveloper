a, b =  ["Anton","Alex", "Dima",'Anton', "Kate", "Galina", "Ivan",'Marie','Denis', 'Anton',"Dima", "Doma", 'dsa', 'Galina', 'Kate', 'Kate', 'Kate', 'Anton','Anton'], ["Dima", "Ivan", "Kate",'Anton']
print('\nOriginal List:', *a, '\n')
print('Substracted List:', *b, '\n\nResult: ', sep=' ', end='')
[print(a[i], end=' ') for i in range(len(a)) if a[i] not in b]
print('\n')
