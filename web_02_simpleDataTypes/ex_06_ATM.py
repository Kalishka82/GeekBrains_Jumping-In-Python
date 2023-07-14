#  Задание No6
# 📌 Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третьей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

START_BALANCE: int = 0
DEPOSIT_FACTOR: int = 50
WITHDRAW_FACTOR: int = 50
WITHDRAW_RATE: float = 0.015
WITHDRAW_RATE_MIN: int = 30
WITHDRAW_RATE_MAX: int = 600
INTEREST_FREQUENCY: int = 3
INTEREST_PERCENT: float = 0.03
TRESHOLD_AMOUNT: int = 5_000_000
WEALTH_TAX: float = 0.1


balance: int = START_BALANCE
count: int = 0

while True:

    if balance > TRESHOLD_AMOUNT:
        balance -= balance * WEALTH_TAX
        print(f'Баланс вашего счета после удержания налога на богатство: {int(balance)}')
    if count % INTEREST_FREQUENCY == 0:
        balance += balance * INTEREST_PERCENT
        print(f'Баланс вашего счета после начисления процентов: {int(balance)}')
    operation = input(f'Для работы с банкоматом выберите действие:\n1 - пополнить\n'
                      f'2 - снять\n3 - выйти\n')
    match operation:
        case '1':
            deposit_amount = int(input(f'Введите сумму пополнения, кратную {DEPOSIT_FACTOR}: '))
            if deposit_amount > 0 and deposit_amount % DEPOSIT_FACTOR == 0:
                balance += deposit_amount
            else:
                print(f'Сумма пополнения не кратна {DEPOSIT_FACTOR}')
            print(f'Баланс вашего счета: {int(balance)}')
            count += 1
        case '2':
            withdraw_amount = int(input(f'Введите сумму снятия, кратную {WITHDRAW_FACTOR}.\n'
                                        f'Нельзя снять больше, чем на счете: '))
            if withdraw_amount % WITHDRAW_FACTOR == 0:
                percent = balance * WITHDRAW_RATE
                if percent < WITHDRAW_RATE_MIN:
                    percent = WITHDRAW_RATE_MIN
                elif percent > WITHDRAW_RATE_MAX:
                    percent = WITHDRAW_RATE_MAX

                if withdraw_amount + percent > balance:
                    print('Недостаточно средств на счете')
                else:
                    balance -= (withdraw_amount + percent)
            else:
                print(f'Сумма пополнения не кратна {WITHDRAW_FACTOR}')
            print(f'Баланс вашего счета: {int(balance)}')
            count += 1
        case '3':
            print(f'Баланс вашего счета: {int(balance)}')
            break
        case _:
            break
