def exit_program():
    print('\nЗавершение программы')
    exit()


def yes_no():
    print('\n1) Да\n'
          '2) Нет\n')
    option = int(input('Введите ваш вариант: '))
    while option > 2 or option < 1:
        option = int(input('Выберете ваш вариант: '))
    return option


def creating_base():
    data = str(input("\nВведите имя файла базы данных: "))
    formate = '.csv'
    with open(data + formate, 'w', encoding='utf-8-sig') as file:
        file.write('id;Имя;Фамилия;Дата рождения;Номер телефона;Должность\n'
                   '0;1;2;3;4;5\n')
    print('\nДля корректной работы программы, будет выполнен автоматический выход')
    exit_program()


def open_base(file_name):
    try:
        formate = '.csv'
        with open(file_name + formate, "r", encoding="utf-8-sig") as file:
            uni_base = file.readlines()
        return uni_base
    except FileNotFoundError:
        print('Такого файла нет. Желаете создать?')
    if yes_no() == 1:
        creating_base()
    else:
        exit_program()


def change_parameters(current_base, change_lst, number):
    try:
        base_line = current_base[change_lst[0]].split(';')
        base_line[number] = change_lst[1]
        base_line = ";".join(map(str, base_line))
        current_base[change_lst[0]] = base_line
        return current_base
    except IndexError:
        print('Такой записи нет')


def add_new_info(current_base, new_info_list):
    new_id_str = current_base[-1].split(';')
    new_id = str(int(new_id_str[0]) + 1)
    result = f'{new_id};{new_info_list[0]};{new_info_list[1]};{new_info_list[2]};{new_info_list[3]};{new_info_list[4]}'
    current_base.append(result)
    return current_base


def delete_row(current_base, number_of_row):
    current_base_list = []
    for i in current_base:
        i = i.split(';')
        current_base_list.append(i)
    current_base_list.pop(number_of_row)
    for j in range(number_of_row, len(current_base_list)):
        current_base_list[j][0] = str(j)
    for k in range(len(current_base_list)):
        current_base_list[k] = ";".join(map(str, current_base_list[k]))
        current_base = current_base_list
    return current_base


def save_base(current_base, file_name):
    formate = '.csv'
    with open(file_name + formate, 'w', encoding='utf-8-sig') as file:
        for i in current_base:
            file.writelines(i)


def display_base(current_base):
    for line in current_base:
        print(line, end='')


def display_row(current_base, row_number):
    try:
        print(current_base[0], current_base[row_number])
    except IndexError:
        print('Такой записи нет')
