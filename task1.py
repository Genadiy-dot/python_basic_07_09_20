'''
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
 Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''
def division_func(param_1, param_2):
    if param_2 == 0:
        print('неопределённость')
        return
    total = param_1 / param_2
    return total


param_1 = float(input("Введите первое число: "))
param_2 = float(input("Введите второе число: "))
print(division_func(param_1, param_2))
