# 1.Пользователь вводит 2 слова. Если последняя буква первого слова совпала с 
# первой буквой второго, то в этом случае необходимо вывести слово “Верно”, в противном случае 
# “Ошибка”. (игра в города) 

# *сделать это циклично (по желанию)
while True:
    w1 = input("Введите слово 1 - ")
    w2 = input("Введите слово 2 - ")
    if w1[-1].lower() == w2[0].lower():
        print("Верно")
    else:
        print("Ошибка")