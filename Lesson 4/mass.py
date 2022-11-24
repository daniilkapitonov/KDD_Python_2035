import random

mass = ['Hello', 'Brother', 'Red', 'Apple', 'Lego', 'Arduino', 'Dota']
print(mass[1])
print('Hello' in mass)
print(mass[1:3])

for i in range(1,5,2):
    print(i, end = " ")
print()

for i in mass[0]:
    print(i, end = " ")

print()
m_num = []
for i in range(26):
    m_num.append(mass[random.randint(1,len(mass))-1])

print(m_num)
