'''
Реализовать два небольших скрипта:
итератор, повторяющий элементы некоторого списка, определенного заранее.
'''
from itertools import cycle

o = 0
for el in cycle(['p', 'y', 't', 'h', 'o', 'n']):
    if o > 20:
        break
    print(el)
    o +=1
