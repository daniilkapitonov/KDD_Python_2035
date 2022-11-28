# 1.Есть массив длинной 25 элементов. Надо его заполнить 
# случайными числами от 1 до 100 и найти сумму всех элементов массива, 
# среднее арфмитическое элементов и отсортировать массив.
import random

mass = []
summ = 0
for i in range(25):
    mass.append(random.randint(1,100))
    summ+=mass[i]


print("Mass - ", mass)
print("Summ - ", summ)
print("Sr. ar. - ",summ/25)
mass.sort()
print("Mass_sort - ", mass)