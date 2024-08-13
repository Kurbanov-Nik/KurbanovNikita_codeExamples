def get_money_for_exchange():
    while True:
        try:
            money = int(input("Введите сумму денег для размена: "))
            if money > 1:
                return money
            else:
                print("Разменивать нечего!")
        except ValueError:
            print("ОШИБКА! Было введено не целое число!")

def show_exchange(exchange):
    for i in range(len(exchange) - 1, -1, -1):
        print(("%d " % banknotes[i]) * exchange[i], end="")
    print()

def reload_exchange(exchange, index, money, banknotes):
    exchange = [0 if i < index else exchange[i] for i in range(0, len(exchange))]
    exchange[0] = money - sum([banknotes[i] * exchange[i] for i in range(0, len(exchange))])
    return exchange

def exchange_money(money, banknotes):
    max_index = 0
    for i, value in enumerate(banknotes):
        if money - value <= 0:
            break
        max_index = i
    exchange = [0 for _ in range(0, max_index + 1)]
    exchange[0] = money
    print("Возможные варианты размена %d руб.:" % money)
    show_exchange(exchange)

    for index in range(1, max_index + 1):
        iter = index
        exchange = reload_exchange(exchange, max_index, money, banknotes)
        while True:
            if exchange[0] - banknotes[iter] < 0:
                if iter + 1 <= index:
                    iter += 1
                    exchange = reload_exchange(exchange, iter, money, banknotes)
                else:
                    break
            else:
                exchange[iter] += 1
                exchange[0] -= banknotes[iter]
                show_exchange(exchange)
                iter = 1

# money = get_money_for_exchange()
money = 17
banknotes = [1, 2, 5, 10, 50, 100]
exchange_money(money, banknotes)