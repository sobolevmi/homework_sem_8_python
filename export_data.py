def export_data_from_file(file_name):
    """Функция по экспорту информации, содержащейся в телефонном справочнике, в другой файл"""
    with open(file_name, "r") as a_file:
        new_file_name = str(input("Введите наименование файла, в который будет экспортирована база "
                                  "данных (.txt):\n"))
        with open(new_file_name, "a") as b_file:
            for line in a_file:
                b_file.write(line)
            a_file.close()
            b_file.close()
    print("Ваши данные успешно экспортированы!\n")