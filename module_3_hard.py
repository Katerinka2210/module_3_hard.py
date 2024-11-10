

data_structure = [[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum(*data_structure):
    s = 0
    for x in data_structure:
        if isinstance(x, (int, float)):
             s += x
        elif isinstance(x, str):
             s += len(x)
        elif isinstance(x, (list, set, tuple)): # если несколько типов, то оборачиваем их в кортеж
            for i in x:    # проходимся по х(который либо кортеж, либо список, либо множество внутри данного списка)
                s += calculate_structure_sum(i)  # вызываем функцию до тех пор, пока не придем к элементарным значениям (либо число, либо строка)
        elif isinstance(x, dict):
            for value, key in x.items(): # проходимся по значениям и ключам внутри словаря и items залезает внутрь словаря и возвращает цикл
                s += calculate_structure_sum(value, key)
    return s


result = calculate_structure_sum(data_structure)
print(result)











