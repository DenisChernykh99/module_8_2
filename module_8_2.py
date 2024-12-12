
def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
    return (result, incorrect_data)

def calculate_average(numbers):
    quan_numbers = 0
    try:
        for quan in numbers:
            try:
                quan / 1
                quan_numbers += 1
            except TypeError:
                print(f'Некорректный тип данных для подсчета {quan}')
        return personal_sum(numbers)[0] / quan_numbers
    except TypeError:
        print('В numbers записан некорректный тип данных')
    except ZeroDivisionError:
        return 0


print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать