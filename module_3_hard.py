def calculate_structure_sum(data):
    if isinstance(data, (int,bool,float)):  #проверка на число, булевый список
        return data
    elif isinstance(data, (str)): #проверка на строку - считаем длдину строки,
        return len(data)
    elif isinstance(data, (list, set, tuple)): #проверка на спиок, кортеж, множество - реукрсие функции поэлементно
        data = list(data)
        if len(data)==0:
            return 0
        elif len(data)==0:
            return calculate_structure_sum(data[0])
        else:
            return (calculate_structure_sum(data[0]) +
                    calculate_structure_sum(data[1:]))
    elif isinstance(data, (dict)): #проверка на словарь - рекурсия на ключи и значения
        key = list(data.keys())
        value = list(data.values())
        return (calculate_structure_sum (key) +
                calculate_structure_sum (value))


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)