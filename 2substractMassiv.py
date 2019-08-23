a =  ["Anton","Alex", "Dima",'Anton', "Kate", "Galina", "Ivan",'Marie','Denis', 'Anton',"Dima", "Doma", 'dsa', 'Galina', 'Kate', 'Kate', 'Kate', 'Anton','Anton']
b = ["Dima", "Ivan", "Kate",'Anton']
print('Original list: ', a)
print('Substracted list: ', b)
a = [x for x in a if x not in b]
print('\nDifference List: ', a)
