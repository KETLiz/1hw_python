# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"

print('Введите 3 числа от 0 до 1: ')
x = int(input())
y = int(input())
z = int(input())

def truth(a, b, c):
    if (not a or b or c) == (not a and not b and not c):
        return truth

print(truth(x, y, z))