'''
Реализовать функцию my_func(),
 которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов
'''
def my_func(arg_1, arg_2, arg_3):
    summ = arg_1 + arg_2 + arg_3    # вычисляем сумму трёх аргументов
    if arg_1 < arg_2 and arg_1 < arg_3:   # сумма двух наибольших=сумма-минимум
        minn = arg_1

    elif arg_2 < arg_1 and arg_2 < arg_3:
        minn = arg_2

    else:
        minn = arg_3

    summ_1 = summ - minn
    return(summ_1)
arg_1 = float(input("Введите первый аргумент: "))
arg_2 = float(input("Введите второй аргумент: "))
arg_3 = float(input("Введите третий аргумент: "))
print(my_func(arg_1,arg_2,arg_3))






