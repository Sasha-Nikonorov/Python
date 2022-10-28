def creating():
    file = 'Phonebook.csv'
    with open(file, 'w', encoding='utf-8') as data:
        data.write(f'id, имя, фамилия, день рождения, место работы, номер телефона, описание\n')
