def start_message():
    print('Перед началом работы необходимо\n'
          '1)Создать\n'
          '2)Открыть\n'
          'базу данных: ', end='')


def open_base_message():
    name = input('Введите имя файла базы данных с разрешением "*.csv": ')
    return name


def base_menu():
    print('\nВыберите необходимое действие:\n'
          '1) Открыть другую базу данных\n'
          '2) Вывод открытой базы данных\n'
          '3) Вывод конкретной строки из открытой базы данных\n'
          '4) Редактирование параметров базы данных\n'
          '5) Добавить новую запись в открытую базу данных\n'
          '6) Удалить запись из открытой базы данных\n'
          '7) Сохранить базу\n'
          '8) Завершить работу\n')
    option = int(input('Введите ваш вариант: '))
    while option > 8 or option < 0:
        option = int(input('Выберете ваш вариант: '))
    return option


def show_row_message():
    row = int(input('Введите id записи для показа: '))
    return row


def show_change_parameter():
    print('\nВыберите какой параметр необходимо изменить:\n'
          '1: Имя\n'
          '2: Фамилия\n'
          '3: Дата рождения\n'
          '4: Номер телефона\n'
          '5: Должность\n'
          '6: Вернуться в главное меню\n')
    parameter = int(input('Выберете ваш вариант: '))
    while parameter > 6 or parameter < 1:
        parameter = int(input('Выберете ваш вариант: '))
    return parameter


def show_change_name():
    change_name_list = []
    name_id = int(input('Для замены параметра "Имя" введите id строки: '))
    new_name = input('Введите новое имя: ')
    change_name_list.append(name_id)
    change_name_list.append(new_name.capitalize())
    return change_name_list


def show_change_second_name():
    change_second_name_list = []
    second_name_id = int(input('Для замены параметра "Фамилия" введите id строки: '))
    new_second_name = input('Введите новую фамилию: ')
    change_second_name_list.append(second_name_id)
    change_second_name_list.append(new_second_name.capitalize())
    return change_second_name_list


def show_change_birth_date():
    change_birth_date_list = []
    birth_date_id = int(input('Для замены параметра "Дата рождения" введите id строки: '))
    temp = False
    while not temp:
        new_birth_date = input('Введите новую дату рождения: ')
        if len(new_birth_date) != 10:
            print('Введите в формате дд.мм.гггг')
        elif new_birth_date[2] != '.' and new_birth_date[5] != '.':
            print('Введите разделитель "."')
        else:
            change_birth_date_list.append(birth_date_id)
            change_birth_date_list.append(new_birth_date)
            temp = True
    return change_birth_date_list


def show_change_phone_number():
    change_phone_number_list = []
    phone_number_id = int(input('Для замены параметра "Номер телефона" введите id строки: '))
    temp = False
    while not temp:
        new_phone_number = input('Введите новый номер телефона: ')
        if len(new_phone_number) != 11:
            print('В номере телефона должно быть 11 цифр.')
        else:
            new_phone_number = int(new_phone_number)
            change_phone_number_list.append(phone_number_id)
            change_phone_number_list.append(new_phone_number)
            temp = True
    return change_phone_number_list


def show_change_job_title():
    change_job_title_list = []
    job_title_id = int(input('Для замены параметра "Должность" введите id строки: '))
    new_job_title = input('Введите новую должность: ')
    change_job_title_list.append(job_title_id)
    change_job_title_list.append(new_job_title.capitalize())
    return change_job_title_list


def show_new_info():
    new_info_list = []
    add_name = input('Введите параметр "Имя" новой записи: ')
    new_info_list.append(add_name.capitalize())
    add_second_name = input('Введите параметр "Фамилия" новой записи: ')
    new_info_list.append(add_second_name.capitalize())
    temp = False
    while not temp:
        add_birth_date = input('Введите параметр "Дата рождения" новой записи: ')
        if len(add_birth_date) != 10:
            print('Введите в формате дд.мм.гггг')
        elif add_birth_date[2] != '.' and add_birth_date[5] != '.':
            print('Введите разделитель "."')
        else:
            new_info_list.append(add_birth_date)
            temp = True
    temp = False
    while not temp:
        add_phone_number = input('Введите параметр "Номер телефона" новой записи: ')
        if len(add_phone_number) != 11:
            print('В номере телефона должно быть 11 цифр.')
        else:
            add_phone_number = int(add_phone_number)
            new_info_list.append(add_phone_number)
            temp = True
    add_job_title = input('Введите параметр "Должность" новой записи: ')
    new_info_list.append(add_job_title.capitalize())
    return new_info_list


def show_delete_info():
    delete_info_id = int(input('Для удаления записи введите id строки: '))
    return delete_info_id


def show_save_base():
    save_base = input('Введите имя файла для сохранения базы данных в формате "name.csv": ')
    return save_base
