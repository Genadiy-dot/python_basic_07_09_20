'''
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
 Для заполнения списка элементов необходимо использовать функцию input()
'''
el_count = int(input("Введите количество элементов списка: "))
my_list = []

index = 0
while index < el_count:
    my_list.append(input("Введите следующее значение списка: ")) # вставка нового элемента конец списка
    index +=1

for i in range(1,el_count,2):    # для каждого нечётного элемента списка
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)

