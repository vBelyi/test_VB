#бульбашкове сортування, в кожній парі чисел порівнює їх і переставляє місцями якщо наступне менше
# n = 6
# mass = [5, 7, 4, 3, 8, 2]
# count = 0
# for run in range(n-1):
#     for i in range (n-1-run):
#         print(f'Сравнение {mass[i]} и {mass[i+1]}')
#         if mass[i] > mass[i+1]:
#             count +=1
#             mass[i], mass[i+1] = mass[i+1], mass[i]
#     print(*mass)
#     print(count)
#
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# ab = a + b
# c = []
# while ab:
#     c.append(ab.pop(ab.index(min(ab))))
# print(*c)

#рекурсія

def rec(x):
    if x > 0:
        print(x-1)
        rec(x-1)
rec(int(input('Input your number: ')))


# def my_string(*args):
#     vovels = ['a', 'e', 'i', 'o', 'u']
#     test = []
#     for index in vovels:
#         counter = args.count(index)
#         test.append(counter)
#     return sum(test)
# print(my_string('elloo'))
#
# my_string = 'heeeeeelllooo'
# vovels = ['a', 'e', 'i', 'o', 'u']
# test = []
# for index in vovels:
#     count = my_string.count(index)
#     test.append(count)
# print(sum(test))


# def my_string(*args):
#     new_string = set(*args)
#     my_vovels = ['a', 'e', 'i', 'o', 'u']
#     new_vovels = set(my_vovels)
#     count = 0
#     for num in new_vovels:
#         if num in new_string:
#             count +=1
#     return count
#
# print(my_string('Helooo'))