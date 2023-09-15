# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление.
# Функцию hex используйте для проверки своего результата.

num = int(input('Введите число в десятичной системе: '))
base = 16
print(f'Проверка встроенной функцией hex: \t{hex(num)[2:]}')

def self_hex(number: int) -> str:
    if not number:
        return '0x0'
    result = ''
    hex_letters = list('0123456789abcdef')
    while number > 0:
        result = hex_letters[number % base] + result
        number //= base
    return result


print(f'Собственная функция self_hex:  {self_hex(num)}')