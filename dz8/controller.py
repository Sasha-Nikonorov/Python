import operations
import user_interface as ui

process = True
ui.start_message()
i = input()
while not i == '1' or not i == '2':
    if i == '1':
        operations.creating_base()
        operations.exit_program()
    elif i == '2':
        base = operations.open_base(ui.open_base_message())
        while process:
            option = ui.base_menu()
            if option == 1:
                base = operations.open_base(ui.open_base_message())
            elif option == 2:
                operations.display_base(base)
            elif option == 3:
                operations.display_row(base, ui.show_row_message())
            elif option == 4:
                parameter = ui.show_change_parameter()
                if parameter == 1:
                    base = operations.change_parameters(base, ui.show_change_name(), parameter)
                elif parameter == 2:
                    base = operations.change_parameters(base, ui.show_change_second_name(), parameter)
                elif parameter == 3:
                    base = operations.change_parameters(base, ui.show_change_birth_date(), parameter)
                elif parameter == 4:
                    base = operations.change_parameters(base, ui.show_change_phone_number(), parameter)
                elif parameter == 5:
                    base = operations.change_parameters(base, ui.show_change_job_title(), parameter)
                else:
                    print()
            elif option == 5:
                base = operations.add_new_info(base, ui.show_new_info())
            elif option == 6:
                base = operations.delete_row(base, ui.show_delete_info())
            elif option == 7:
                operations.save_base(base, ui.show_save_base())
            else:
                print('Вы сохранили данные?')
                option = operations.yes_no()
                if option == 1:
                    operations.exit_program()
                if option == 2:
                    operations.save_base(base, ui.show_save_base())
    else:
        i = input('Повторите ввод: ')
