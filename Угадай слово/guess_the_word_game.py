import random
import re

words_list = ["сфера",
              "клоун",
              "паразитология",
              "вменяемость",
              "выигрыш",
              "носок",
              "абракадарбра"]

word = random.choice(words_list)
max_attempts = 8
attempts_counter = 0
entered_letters = []
solution = "".join(["*" for _ in word])

def display_entered_letters():
    print("Вот список всех ранее введенных букв:")
    for sym in entered_letters:
        print(sym, end=" ")

input_check = re.compile(r"^[А-ЯЁа-яё]$")

print("Угадайте слово\n%s" % solution)
while True:
    symbol = input("Введите букву: ")

    if input_check.search(symbol):
        if symbol in entered_letters:
            print("Такая буква уже была!")
            display_entered_letters()
        elif symbol in word:
            symbol_check = re.compile(r"%s" % symbol)
            entered_letters.append(symbol)
            for sym in symbol_check.finditer(word):
                solution = solution[0:sym.start()] + symbol + solution[sym.start() + 1:]
        else:
            attempts_counter += 1
            entered_letters.append(symbol)
            print("Такой буквы нету в слове. Осталось %d попыток" % (max_attempts - attempts_counter))
            if attempts_counter > max_attempts:
                print("Количество попыток исчерпано. Вы проиграли!")
                break
    else:
        print("Вы ввели что-то странное...")
        display_entered_letters()

    print(solution)
    if "*" not in solution:
        print("Вы выиграли!")
        break