from random import *
words = ['гитара', 'банан', 'карандаш', 'лимон', 'кот', 'машина', 'радуга', 'солнце', 'телефон', 'яблоко']
word = words[randint(0, len(words)-1)]
life = len(word) + 5
user_know = ["_"] * len(word)
find_letter = 0

print("Количество жизней:", life)

print("_" * len(word))

while life != 0 and word != "".join(user_know):
    letter = input("Введи новую букву ")
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                user_know[i] = letter
        print("".join(user_know))


    else:
         life -= 1
         print('Попробуй снова. Еще не все потеряно. Или всё...)', "Осталось", life, "жизней.")

print("Молодец! Отгадал.")