import logger


def add_employees():
    """Функция по добавлению новых сведений о сотрудниках компании в базу данных"""
    employees_dict = {
        "boss": "руководитель",
        "worker": "сотрудник"
    }
    with open("employees.txt", "a") as file:
        employees_password = str(input("Введите пароль: "))
        if employees_password == "boss":
            employee_surname = str(input("Введите фамилию сотрудника: "))
            file.write(employee_surname + " *** ")
            employee_name = str(input("Введите имя сотрудника: "))
            file.write(employee_name + " *** ")
            employee_patronymic = str(input("Введите отчество сотрудника. Если у сотрудника нет отчетства, нажмите Enter: "))
            file.write(employee_patronymic + " *** ")
            employee_sex = str(input("Введите пол сотрудника в формате 'муж' или 'жен': "))
            file.write(employee_sex + " *** ")
            employee_date_of_birth = str(input("Введите дату рождения сотрудника в формате 'день.месяц.год': "))
            file.write(employee_date_of_birth + " *** ")
            employee_place_of_birth = str(input("Введите место рождения сотрудника: "))
            file.write(employee_place_of_birth + " *** ")
            employee_job_title = str(input("Введите наименование должности сотрудника: "))
            file.write(employee_job_title + "\n")
            print("Данные о сотруднике успешно сохранены\n")
        if employees_password == "worker":
            print("У вас нет прав доступа на добавление информации о новых сотрудниках\n")
            logger.log_message("error")
        elif employees_password != "boss" and employees_password != "worker":
            print("Введен неправильный пароль\n")
            logger.log_message("critical")


def view_employees():
    """Функция по просмотру хранящейся в базе данных информации о сотрудниках компании"""
    employees_dict = {
        "boss": "руководитель",
        "worker": "сотрудник"
    }
    system_password = str(input("Введите пароль: "))
    if system_password == "boss":
        user_choice = str(input("Если вы хотите просмотреть данные обо всех сотрудниках, нажмите 1\n"
                                "Если вы хотите просмотреть данные о конкретном сотруднике, нажмите 2\n"))
        with open("employees.txt", "r") as file:
            if user_choice == "1":
                for line in file:
                    print(line)
            elif user_choice == "2":
                info = str(input("Введите данные сотрудника для поиска: "))
                for line in file:
                    if info.lower() in line.lower():
                        print(line)
            else:
                while user_choice != "1" and user_choice != "2":
                    user_choice = str(input("Вы ввели неверное число. Попробуйте снова\n"))
                    logger.log_message("warning")
    if system_password == "worker":
        with open("employees.txt", "r") as file:
            info_employee = str(input("Введите вашу фамилию для поиска: "))
            for line in file:
                if info_employee.lower() in line.lower():
                    print(line)
    if system_password not in employees_dict:
        print("Вы ввели неправильный пароль")
        logger.log_message("critical")
