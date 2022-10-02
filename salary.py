import logger


def add_employees_salary():
    """Функция по добавлению новых сведений о заработной плате сотрудников компании"""
    salary_dict = {
        "boss": "руководитель",
        "worker": "сотрудник",
        "money": "бухгалтерия"
    }
    salary_password = str(input("Введите пароль: "))
    if salary_password == "boss" or salary_password == "money":
        with open("salary.txt", "a") as file:
            salary_employee_surname = str(input("Введите фамилию сотрудника: "))
            file.write(salary_employee_surname + " *** ")
            salary_employee_name = str(input("Введите имя сотрудника: "))
            file.write(salary_employee_name + " *** ")
            salary_employee_patronymic = str(input("Введите отчество сотрудника. Если у сотрудника нет отчетства, нажмите Enter: "))
            file.write(salary_employee_patronymic + " *** ")
            salary_job_title = str(input("Введите должность сотрудника: "))
            file.write(salary_job_title + " *** ")
            salary_size = str(input("Введите размер оклада сотрудника (в рублях РФ): "))
            file.write(salary_size + " *** ")
            salary_bonus = str(input("Введите размер премии сотрудника (в рублях РФ): "))
            file.write(salary_bonus + "\n")
            print("Данные о сотруднике успешно сохранены\n")
    elif salary_password == "worker":
        print("У вас нет прав доступа на добавление информации о новых сотрудниках\n")
        logger.log_message("error")
    elif salary_password not in salary_dict:
        print("Введен неправильный пароль\n")
        logger.log_message("critical")


def view_salary():
    """Функция по просмотру сведений о заработной плате сотрудников компании"""
    dict_salary = {
        "boss": "руководитель",
        "worker": "сотрудник",
        "money": "бухгалтерия"
    }
    password_salary = str(input("Введите пароль: "))
    with open("salary.txt", "r") as file:
        if password_salary == "boss" or password_salary == "money":
            user_choice = str(input("Если вы хотите просмотреть данные о заработной плате всех сотрудников, нажмите 1\n"
                                    "Если вы хотите просмотреть данные о заработной плате конкретного сотрудника, нажмите 2\n"))
            with open("salary.txt", "r") as file:
                if user_choice == "1":
                    for line in file:
                        print(line)
                elif user_choice == "2":
                    info_worker_salary = str(input("Введите данные сотрудника для поиска: "))
                    for line in file:
                        if info_worker_salary.lower() in line.lower():
                            print(line)
                else:
                    while user_choice != "1" and user_choice != "2":
                        user_choice = str(input("Вы ввели неверное число. Попробуйте снова\n"))
                        logger.log_message("warning")
        elif password_salary == "worker":
            worker_name = str(input("Введите ваши данные для поиска: "))
            for line in file:
                if worker_name.lower() in line.lower():
                    print(line)
        elif password_salary not in dict_salary:
            print("Введен неправильный пароль\n")
            logger.log_message("critical")
