import random

text = 'С Новым Годом ФМ!'
n = 0
while n < 10:
    try: n = int(input('Введите целое число\nне меньше 10(это размер елки)\n: '))
    except: pass

a = [[], [], []]
for s in range(3):
    for i in range(1, n + 1 - s * 2):
        if s == 1 and i == n // 2:
            space = (6 * i - 5 - len(text)) // 2
            color = '\033[1;34m'
            style = '\033[3m'
            a[s].append(
                '   ' * (n - i) + ' ' * space +
                style + color + text +
                '\033[0m' + '\033[23m')
        else:
            f = ''
            for _ in range(6 * i - 5):
                f += 'O' if random.randint(0, 10) == 0 else '*'
            a[s].append('   ' * (n - i) + f)

for stage in [a[2], a[1], a[0]]:
    for s in stage:
        for c in s:
            if c == '*': print('\033[1;32m*\033[0m', end='')
            elif c == 'O': print('\033[1;33m@\033[0m', end='')
            else: print(c, end='')
        print()

color = '\033[1;31m'
space = (len(a[0][-1]) - n // 4) // 2
size = (n // 3)
for _ in range(n // 4):
    print(' ' * space + (color + '*' + '\033[0m') * size)
