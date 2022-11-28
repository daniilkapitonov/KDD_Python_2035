mass = [1,2,3] #Можем: добавить, удалить, изменить, считать (list)
print(type(mass))

cort = (1,2,3) #Можем: считать (tuple кортеж)
print(type(cort))

set_m = {1,2,3,1,2,3, "hello", "hello"} #Можем: считать, нет индексов, нет повторяющихся элементов (set)
print(type(set_m))
print(set_m)


# 2number = 2 Так нельзя
# number_2 = 2 
# num = 2 
# n2 = 2 

# a = int(input())
# b=2
# print(a+b)

# mass[-1] = 3

word = "Moscow"
print(word[1:6:2]) #range(1,6,2)

dict_m = {'Москва':5,"Питер":4, "Казань":8, "Старый оскол":10, 5:"Москва"}
print(type(dict_m))
print(dict_m["Питер"]+dict_m["Казань"])
print(dict_m[5])
dict_m[10] = "Десять"
print(dict_m)

s = "1, 2, 3, 41"
m = s.split(", ")
print(m)

print(s.count("1"))