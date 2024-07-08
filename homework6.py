my_dict = {'grecha': 1, 'muka': 2}
print(my_dict)
print(my_dict['grecha'])
print(my_dict.get('pivo'))
#my_dict['sahar'] = 3
#my_dict['manka'] = 43
my_dict.update({'sahar': 3, 'manka': 23})
print(my_dict)
my_dict.pop('muka')
print(my_dict)
my_set = {1, 3.1, 'poop', True, 1, 'poop', 3.1}
print(my_set)
my_set.add(5)
my_set.add('bebra')
print(my_set)
my_set.remove(1)
print(my_set)