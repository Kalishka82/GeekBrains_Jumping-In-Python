#  Задание No2
# 📌 Напишите программу, которая принимает две строки вида “a/b” — дробь с числителем
# и знаменателем. Программа должна возвращать сумму и произведение дробей.
# 📌 Для проверки своего кода используйте модуль fractions.

import re
import math
import fractions

fracs = list(map(int,
                 re.split(" |/", input('Input two fractions like 2/3 throw the space: '))))

sum_div = fracs[0] * fracs[3] + fracs[2] * fracs[1]
sum_denom = fracs[1] * fracs[3]
sum_nod = math.gcd(sum_div, sum_denom)
if sum_denom / sum_nod != 1:
    sum_fracs = str(int(sum_div / sum_nod)) + '/' + str(int(sum_denom / sum_nod))
else:
    sum_fracs = str(int(sum_div / sum_nod))

prod_div = fracs[0] * fracs[2]
prod_denom = fracs[1] * fracs[3]
prod_nod = math.gcd(prod_div, prod_denom)
if prod_denom / prod_nod != 1:
    prod_fracs = str(int(prod_div / prod_nod)) + '/' + str(int(prod_denom / prod_nod))
else:
    prod_fracs = str(int(prod_div / prod_nod))


print(sum_fracs, prod_fracs)

f1 = fractions.Fraction(fracs[0], fracs[1])
f2 = fractions.Fraction(fracs[2], fracs[3])
print(f1 + f2, f1 * f2)
