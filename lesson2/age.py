def activity_type(age):
    if age in range(0, 7):
        return 'Нужно ходить в детский сад'
    elif age in range(7, 17):
        return 'Нужно ходить в школу'
    elif age in range(17, 20):
        return 'Нужно учиться в ВУЗе'
    elif age > 20:
        return 'Придётся ходить на работу =('
    else:
        return 'Какой-то неправильный возраст'


persons_age = int(input('Введите возраст: '))
activity = activity_type(persons_age)
print(activity)
