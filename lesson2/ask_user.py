def ask_user():
    dictionary = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую', 'Хорошо': 'У меня тоже, пока!'}
    while True:
        try:
            answer = input('Как дела?\n')
            if answer in dictionary:
                print(dictionary[answer])
            if answer == 'Хорошо':
                break
        except KeyboardInterrupt:
            print('Пока')
            break


ask_user()

