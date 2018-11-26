def get_summ(num_one, num_two):
    try:
        num_one = int(num_one)
        num_two = int(num_two)
        return num_one + num_two
    except ValueError:
        return 'Какие-то плохие числа'


number_one = input('Введите первое число: ')
number_two = input('Введите второе число: ')
print(get_summ(number_one, number_two))
