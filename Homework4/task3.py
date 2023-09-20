# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

import decimal

PERCENT_FOR_TAKE_OFF = 0.015
LOWER_LIMIT_FOR_PERCENT = 30
UPPER_LIMIT_FOR_PERCENT = 600
FREQUENCY_RATE_SUM = 50
RICH_LIMIT = 5_000_000
RICH_LIMIT_PERCENT = 0.1
PERCENT_FOR_OPERATIONS = 0.03
FREQUENCY_RATE_OPS = 3


def log_in_file(name_operation, sum_of_operation, total_sum):
    wf = open('log_file.txt', 'a', encoding='utf-8')
    wf.write(
        f"{name_operation} - {sum_of_operation} у.е. Баланс - {total_sum}\n")
    wf.close()


def give_in(total_sum, input_sum):
    total_sum += input_sum
    return total_sum


def take_off(total_sum, input_sum, percent):
    total_sum = total_sum - input_sum - percent
    print(f"Обратите внимание! \
За операцию списан процент в размере {percent:.2f} у.е.")
    log_in_file("Процент за сняте", percent, total_sum)
    return total_sum


def print_balance(balance):
    print(f"Ваш баланс составляет {balance:.2f} у.е.")


def check_input(input_sum):
    if input_sum <= 0 or input_sum % FREQUENCY_RATE_SUM != 0:
        return False
    return True


def check_take_off(input_sum, total_sum, percent):
    if input_sum + percent > total_sum:
        return False
    return True


def check_to_rich(total_sum):
    if total_sum > RICH_LIMIT:
        return True
    return False


def check_to_count(count_operations):
    if count_operations % FREQUENCY_RATE_OPS == 0:
        return True
    return False


def give_in_operation(total_sum, count_operations):
    while True:
        sum_for_give_in = int(input(f"Какую сумму желаете внести? \
Введите значение, кратное {FREQUENCY_RATE_SUM}: "))
        if check_input(sum_for_give_in):
            total_sum = give_in(total_sum, sum_for_give_in)
            total_sum = give_percent_for_operations(
                total_sum, count_operations)
            print_balance(total_sum)
            log_in_file("Пополнение", sum_for_give_in, total_sum)
            return total_sum
        else:
            print("Неверный ввод! Попробуйте еще раз!")
            print_balance(total_sum)


def take_off_operation(total_sum, count_operations):
    while True:
        sum_for_take_off = int(input(f"Какую сумму желаете снять? \
Введите значение, кратное {FREQUENCY_RATE_SUM}: "))
        if check_input(sum_for_take_off):
            percent_for_take = percent_for_take_off(sum_for_take_off)
            if check_take_off(sum_for_take_off, total_sum, percent_for_take):
                total_sum = take_off(
                    total_sum, sum_for_take_off, percent_for_take)
                total_sum = give_percent_for_operations(
                    total_sum, count_operations)
                print_balance(total_sum)
                log_in_file("Снятие", sum_for_take_off, total_sum)
                return total_sum
            else:
                print("Запрашиваемая сумма превышает баланс счёта!")
                print_balance(total_sum)
        else:
            print("Сумма должна быть кратна 50!")
            print_balance(total_sum)


def percent_for_take_off(sum_for_take_off):
    percent = decimal.Decimal(sum_for_take_off * PERCENT_FOR_TAKE_OFF)
    if percent <= LOWER_LIMIT_FOR_PERCENT:
        percent = LOWER_LIMIT_FOR_PERCENT
    elif percent >= UPPER_LIMIT_FOR_PERCENT:
        percent = UPPER_LIMIT_FOR_PERCENT
    return percent


def percent_for_rich(total_sum):
    if check_to_rich(total_sum):
        print(f"Баланс вашего счета превышает {RICH_LIMIT}! \
Будет списано {RICH_LIMIT_PERCENT * 100:.2f} % от суммы остатка!")
        sum_percent_out = total_sum * (1 - RICH_LIMIT_PERCENT)
        log_in_file("Налог на богатство", sum_percent_out, total_sum)
        return sum_percent_out
    return total_sum


def give_percent_for_operations(total_sum, count_operations):
    if check_to_count(count_operations):
        print(f"За третью совершенную финансовую операцию \
Вам начислено {PERCENT_FOR_OPERATIONS * 100:.2f} % от суммы остатка")
        sum_percent_out = total_sum * (1 + PERCENT_FOR_OPERATIONS)
        log_in_file("Начисление за третью операцию", sum_percent_out, total_sum)
        return sum_percent_out
    return total_sum


def main_menu(total_sum, count_operations):
    total_sum = percent_for_rich(total_sum)
    while True:
        print("Для выбора действия нажмите кнопу:\n\
\t1 - Пополнение счета\n\
\t2 - Снятие наличных\n\
\t3 - Показать баланс\n\
\t4 - Выход")
        input_menu = int(input())
        match input_menu:
            case 1:
                return give_in_operation(total_sum, count_operations)
            case 2:
                return take_off_operation(total_sum, count_operations)
            case 3:
                print_balance(total_sum)
                return total_sum
            case 4:
                print("До новых встреч!")
                exit()
            case _:
                "Неверный ввод"


sum = 0
count_ops = 1
while True:
    temp = sum
    sum = main_menu(sum, count_ops)
    if temp != sum:
        count_ops += 1