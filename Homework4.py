""" Основний рівень
# 1. Перерахувати особливості мови Python
# 	- інтерпретуєма
#   - кросплатформенна та універсальна
# 	- з динамічною типізацією
# 	- наявна велика кількість готових бібліотек
#   - наявність PEP
#   - Open Source"""

"""2. Коротко пояснити основні правила іменування змінних у Python, навести приклади коректних та некоректних назв змінних.
- з малої літери
- Не повинна починатися з великої літери або числа
- без пробілів
- підкреслювання замість пробілів.
 Коректні: abc, a_b_c, abc1. Некоректні: Abc, A b c, 1ABC."""


# 3. Виправити наступний фрагмент кода, щоб не виникало помилки при виконанні:

major_version = 3
minor_version = .9
version = major_version + minor_version
language = 'Python'
language_version = language + ' ' + str(version)
print("language_version")

# 4. З використанням циклу while та оператора розгалуження if (без використання range, for і т.д.) написати код,
# який обраховує суму всіх чисел, менших за 100, які діляться без залишку одночасно на 3 та 5.
n = 0
i = 0
while n < 100:
    n += 1
    if n % 3 == 0 and n % 5 == 0:
        i += n
print(i)

""" 5. Факторіал числа n - добуток всіх цілих позитивних чисел, які менші або дорівнюють n. Наприклад, 3! = 1*2*3 = 6.
 Знайти факторіал числа, яке дорівнює довжині прізвища студента. Результат вивести у вигляді рядка “5! = 120”.
 Реалізація з використанням циклу while."""

surname = input("Введіть, будь ласка, прізвище: ")
sur_len = len(surname)
n = 1
i = 1
while n <= sur_len:
    i *= n
    n += 1
print(str(sur_len) + '! = ', str(i))

""" 6. За допомогою цикла while реалізувати код, який буде на кожному проході циклу відкидати останній символ із заданого
рядка (наприклад, string_to_truncate = 'I have a beautiful cat!') і виводити оновлений рядок, доки рядок не стане пустим.
Коли рядок стане пустим - вивести повідомлення "Nothing's left here"""

string = input("Введіть, будь ласка, рядок: ")
while len(string) > 1:
    string = string[0:len(string) - 1]
    print(string)
else:
    print("Nothing's left here")

"""#===============================================================================
 Просунутий рівень
 1. Які переваги і недоліки виходять з того, що Python є інтерпретованою мовою програмування?
    До переваг можна віднести: Відкритий код, чистий синтаксис, гнучкість і швидкість розробки.
    До недоліків - потреба більших ресурсів для запуску ПО.

 2. Пояснити різницю між мутабельними та імутабельними типами даних.
    Мутабельні - можна змінювати. Імутабельні - незмінні."""

# 3. Прості числа - це такі числа, які діляться без залишку тільки на 1 та самих себе.
# З використанням тільки циклу while та оператора розгалуження if (без циклу for та range), реалізувати код,
# який визначатиме чи є задане число number простим.

number = int(input("Write number: "))
start = True
i = 2
while i <= int(number)**(1/2):
    if number % i == 0:
        start = False
        break
    i += 1
if start:
    print("Prime number")
else:
    print("Composite number")

# 4. Послідовність Фібоначчі - ряд чисел, кожен новий елемент якого визначається як сума двох попердніх елементів.
# Послідовніть Фібоначчі починається так: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...
# З використанням тільки циклу while та оператора розгалуження if (без циклу for та range),
# реалізувати код, який знаходить суму всіх непарних чисел із послідовності Фібоначчі, що менші 100_000.

num = 0
num2 = 1
i = 0
while num < 100000:
    if num % 2 != 0:
        i += num
    num_i = num + num2
    num = num2
    num2 = num_i
print(i)

#Task about  BMI

lower_bound = 18.5
upper_bound = 25
weight = 80     #float(input("What is Your weight (kg)? : "))
height = 1.83   #float(input("What is Your height (m)? : "))
bmi = weight/height**2
if height != 0:
    if bmi < lower_bound:
        print("Your BMI is less than normal!")
    elif lower_bound <= bmi <= upper_bound:
        print("Your BMI is normal!")
    else:
        print("Your BMI is greater than normal!")
