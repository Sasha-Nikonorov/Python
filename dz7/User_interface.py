def get_info():
    info = []
    i_d = int(input('Введите ID: '))
    info.append(i_d)
    first_name = input('Введите имя: ')
    info.append(first_name.capitalize())
    last_name = input('Введите фамилию: ')
    info.append(last_name.capitalize())
    temp = False
    while not temp:
        birthday = input('Введите день рождения в формате дд.мм.гг: ')
        if len(birthday) != 8:
            print('Введите в формате дд.мм.гг')
        elif birthday[2] != '.' and birthday[5] != '.':
            print('Введите разделитель "."')
        else:
            info.append(birthday)
            temp = True
    place_of_work = input('Введите место работы: ')
    info.append(place_of_work)
    temp = False
    while not temp:
        phone_number = input('Введите номер телефона: ')
        if len(phone_number) != 11:
            print('В номере телефона должно быть 11 цифр.')
        else:
            phone_number = int(phone_number)
            info.append(phone_number)
            temp = True

    description = input('Введите описание: ')
    info.append(description)
    return info
