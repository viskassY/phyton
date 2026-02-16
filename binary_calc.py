def binary_calculator(a, b, operation):
    if not (0 <= a <= 255 and 0 <= b <= 255):
        return "Error: numbers must be in range 0-255"

    if operation == '+':
        res = a + b
    elif operation == '-':
        res = a - b
    elif operation == '*':
        res = a * b
    else:
        return "Невідома операція"

    if res < 0 or res > 255:
        return f"Результат {res} поза межами 8-бітної системи (0-255)"

    binary_res = format(res, '08b')
    return f"Результат: {res}. У двійковій системі: {binary_res}"

num1 = int(input("Введіть перше число (0-255): "))
num2 = int(input("Введіть друге число (0-255): "))
op = input("Введіть операцію (+, -, *) : ")

print(binary_calculator(num1, num2, op))