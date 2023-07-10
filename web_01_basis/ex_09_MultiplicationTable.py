# Задание No9
# 📌 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

MIN_FACTOR = 2
MAX_FACTOR = 10

print(16 * ' ', 'ТАБЛИЦА УМНОЖЕНИЯ')
print()

for i in range(MIN_FACTOR, MAX_FACTOR + 1):
    for j in range(MIN_FACTOR, MAX_FACTOR // 2 + 1):
        if i == MAX_FACTOR:
            print(f'{j} X{i} =', i * j, end='    ')
        elif i * j >= MAX_FACTOR:
            print(f'{j} X {i} =', i * j, end='    ')
        else:
            print(f'{j} X {i} = ', i * j, end='    ')
    print()
print()

for i in range(MIN_FACTOR, MAX_FACTOR + 1):
    for j in range(MAX_FACTOR // 2 + 1, MAX_FACTOR):
        if i == MAX_FACTOR:
            print(f'{j} X{i} =', i * j, end='    ')
        elif i * j >= MAX_FACTOR:
            print(f'{j} X {i} =', i * j, end='    ')
        else:
            print(f'{j} X {i} = ', i * j, end='    ')
    print()
print()
