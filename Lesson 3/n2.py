word = input("Введите слово - ")
# word[4] - не вызовет ошибки
if len(word) >=5:
    print(word[4])
else:
    print("НЕТ")