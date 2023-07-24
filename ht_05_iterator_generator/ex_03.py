#  Задание No3
# 📌 Создать функцию генератор чисел Фибоначчи (см. Википедию)

N = 10


def gen_fibonacci(n):
    a = b = 1
    for _ in range(n):
        yield a
        a, b = b, a + b


for i in gen_fibonacci(N):
    print(i, end=' ')

# fib_iter = iter(gen_fibonacci(N))
# for _ in range(N):
#     print(next(fib_iter))
