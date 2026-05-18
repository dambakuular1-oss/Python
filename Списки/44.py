lst = [1, 2, 3, 4, 5]
lst[1] = '10'
print(lst) # выведет [1, '10', 3,4,5]

lst = ['a', 'b', 'c', 'd']
lst[-1] = True  
print(lst)  # Выведет: ['a', 'b', 'c', True]

lst1 = [1, 2, 3]
lst2 = ['a', 'b', 'c']
lst1[-1] = lst2[-1]
print(lst1)  # Выведет: [1, 2, 'c']