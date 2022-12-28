#___________________________1____________________________________
#  Вычислить число c заданной точностью d
# Пример:
# - при $d = 0.001, π = 3.141.$    $10^{-1} ≤ d ≤10^{-10}$

# b = input('b= ')
# d = b.split(sep='.')
# c =len(d[1])
# p = 3.141592653589793238462643383279
# print(round(p,c))

#___________________________2____________________________________
# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.
# n = int(input('N= '))
# list_mnog = []
# c = 2
# while c*c <= n:
#     if n % c == 0:
#         list_mnog.append(c)
#         n = n // c
#     else:
#         c += 1
# list_mnog.append(n)
# print(list_mnog)

#__________________________3_______________________________________
#Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов 
# исходной последовательности.

# pos = input('numbers = ').split()
# list_pos = list(map(int,pos))
# list_uniq = []
# count = list_pos[0]
# for i in list_pos:
#     count = 0
#     for j in list_pos:
#         if i == j:
#             count+=1
#     if count == 1:
#         list_uniq.append(i)
# print(list_uniq)

#_______________________4_____________________________
#Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
#
# import random
# k = int(input('Введите степень: '))
# list_kof = []
# for i in range(k):
#     list_kof.append(str(random.randint(0,100)))
# list_mnog = []
# for i in range(k,-1,-1):
#     if i > 1:
#         list_mnog.append(f"{list_kof[i-1]}x^{i}")
#     elif i == 1:
#         list_mnog.append(f"{list_kof[i-1]}x")
#     elif i == 0:
#         list_mnog.append(list_kof[i-1])
# print("+".join(list_mnog))

#______________________5____________________________
#Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
# data = open('text.txt', 'r')
# for line in data:
#     list_f = line.split(sep='+')
# data.close
# data = open('tex2.txt','r')
# for line in data:
#     list_s = line.split(sep='+')
# data.close
# list_f2 = []
# for i in list_f:
#     list_f2.append(i.split(sep='x'))
# list_s2 = []
# for i in list_s:
#     list_s2.append(i.split(sep='x'))
# list_final = []

# for i in range(len(list_f)):
#     if len(list_f)>i+2:
#         list_final.append(f"{(int(list_f2[i][0])+int(list_s2[i][0]))}x^{len(list_f)-1-i}")
#     elif len(list_f) == i + 2:
#         list_final.append(f"{(int(list_f2[i][0])+int(list_s2[i][0]))}x")
#     elif len(list_f) == i + 1:
#         list_final.append(f"{(int(list_f2[i][0])+int(list_s2[i][0]))}")
# print("+".join(list_final))