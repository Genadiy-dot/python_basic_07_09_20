'''
Реализовать функцию my_func(),
 которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов
'''
def my_func(arg_1, arg_2, arg_3):
    sum = arg_1 + arg_2 + arg_3
    if arg_1 < arg_2 and arg_1 < arg_3:
        min = arg_1

    elif arg_2 < arg_1 and arg_2 < arg_3:
        min = arg_2

    else:
        min = arg_3

    sum_1 = sum - min
    return(sum_1)
arg_1 = float(input("Введите первый аргумент: "))
arg_2 = float(input("Введите второй аргумент: "))
arg_3 = float(input("Введите третий аргумент: "))
print(my_func(arg_1,arg_2,arg_3))






