# print('Введите отзыв (off - завершить):')

# while True:
#     txt = input('')
#     print('Спасибо за обратную связь!\n'
#           'Введите отзыв (off - завершить)')
#     if txt.lower() == 'off':
#         break

# print('Спасибо за сотрудничество')

# price = int(input('Введите цену (0 - завершить):'))
# totalPrice = 0
# while price > 0:
#     totalPrice += price*0.9
#     price = int(input('Введите цену (0 - завершить):'))
# print(totalPrice)

# price = float(input('Введите цену (0 - для завершения):'))
# totalPrice = 0
# while price != 0.0:
#     totalPrice += price
#     price = float(input('Введите цену (0 для завершения):'))
# if totalPrice != 0:
#     print(f'Акция цены пополам\nК оплате {totalPrice/2}')
# else:
#     print(totalPrice)

#3

import random

lis = []

for i in range(10):
    lis.append(random.randint(-51, 51))

print(lis)

def changeMax(lis):

    itemX = max(lis)
    indexX = lis.index(itemX)


    if(indexX == 0):
        pass
    else:
        tmp = lis[0]
        lis.pop(indexX)
        lis.insert(0, itemX)
        lis.pop(1)
        lis.insert(indexX, tmp)

    return lis

def changeMin(lis):
    itemN = min(lis)
    indexN = lis.index(itemN)
    if(indexN == 9):
        pass
    else:
        tmp = lis[9]
        lis.pop(9)
        lis.insert(indexN, tmp)
        lis.pop(indexN+1)
        lis.append(itemN)
    return lis

def summOfFive(lis):
    summ = 0
    for i in lis:
        if i % 5 == 0:
            summ += i
    return summ

def sumOfNegative(lis):
    summ = 0
    for i in lis:
        if (i < 0) and (i % 2) != 0:
            summ += i
    return summ

def sumAndValue(lis):
    summ = 0
    count = 0
    for i in lis:
        if i % 5 == 0 and i % 7 != 0:
            summ += i
            count += 1
    return (summ, count)


lis = changeMax(lis)
lis = changeMin(lis)
sum_five = summOfFive(lis)
sum_negative = sumOfNegative(lis)
summ, count = sumAndValue(lis)

print(lis)
print(f' Сумма кратных 5: {sum_five}\n Сумма отрицательных и нечетных: {sum_negative}')
print(f' Количество чисел кратных 5 и не кратных 7: {count}; и их сумма: {summ}')