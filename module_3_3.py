# 1
print(f'----------')
def print_params(a=1, b='строка',c=True):
    print(a, b, c)

print_params()
print_params(b=25)
print_params(a='Проверка,', c='работает!')
print_params(c=[1,2,3])

# 2
print(f'----------')
values_list = [99.2, False, 'Вероятность']
values_dict = {'a': 'Шрэк', 'b': 1999, 'c': 121.22}
print_params(*values_list)
print_params(**values_dict)

# 3
print(f'----------')
values_list_2 = [77.77, 'Дробь:88/188']
print_params (*values_list_2, 42 )
values_list_2 = [54.32, 'Строка' ]
print_params (*values_list_2, 42 )