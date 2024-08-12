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

def exchange_money(money, banknotes):
    max_index = 0
    for i, value in enumerate(banknotes):
        if money - value <= 0:
            break
        max_index = i

    index = 1
    yield [1 for _ in range(money)]
    while index <= max_index:
        exchange = [1 for _ in range(money)]
        mark = 0
        iter = index

        while True:
            if sum(exchange[mark : ]) - banknotes[iter] < 0:
                if iter + 1 <= index:
                    iter += 1
                    if exchange.count(banknotes[iter]):
                        mark = exchange.index(banknotes[iter]) + exchange.count(banknotes[iter])
                    else:
                        indexes = [(val, exchange.index(val)) for val in set(exchange)]
                        indexes.reverse()
                        for val in indexes:
                            if val[0] < banknotes[iter]:
                                mark = val[1]
                                break
                            mark = val[1] + exchange.count(val[0])
                    exchange = exchange[0: mark] + [1 for _ in range(money - sum(exchange[0 : mark]))]
                else:
                    break
            else:
                exchange = exchange[0 : mark] + [banknotes[iter]]
                mark += 1
                exchange = exchange + [1 for _ in range(money - sum(exchange[0 : mark]))]
                yield exchange
                iter = 1

        index += 1

banknotes = [1, 2, 5, 10, 50, 100]
# money = get_money_for_exchange()
money = 17
g = exchange_money(money, banknotes)
print("Возможные варианты размена %d руб.:" % money)
for i in g:
    print(i)
