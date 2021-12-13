print('Режем число на части')

# Программа, получает на вход число
# и выводит на экран каждую его цифру отдельно
# (каждая цифра в новой строчке).
# Затем выводится число в обратном порядке

num = int(input('Введите число: '))

num_reverse = ''

DIGIT_LAST = 10
divider = 1

digit = num // divider % DIGIT_LAST

while digit != 0:
    num_reverse += str(digit)
    divider *= 10
    print(digit)
    digit = num // divider % DIGIT_LAST

print(num_reverse)

# a = num // 1000
# b = num // 100 % 10
# c = num // 10 % 10
# d = num % 10

# print(f'{a}\n{b}\n{c}\n{d}\nВ обратном порядке: {d}{c}{b}{a}')
