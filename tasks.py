import logger


def add_tasks():
    """Функция по добавлению сведений о новых рабочих задачах в базу данных"""
    tasks_dict = {
        "boss": "руководитель",
        "worker": "сотрудник"
    }
    with open("tasks.txt", "a") as file:
        user_password = str(input("Введите пароль: "))
        if user_password == "boss":
            task_name = str(input("Введите наименование задачи: "))
            file.write(task_name + " *** ")
            task_content = str(input("Введите содержание задачи: "))
            file.write(task_content + " *** ")
            task_performer = str(input("Введите имя исполнителя: "))
            file.write(task_performer + " *** ")
            task_time = str(input("Введите срок исполнения задачи: "))
            file.write(task_time + "\n")
            print("Данные о новой задаче успешно сохранены\n")
        elif user_password == "worker":
            print("У вас нет прав доступа на добавление информации о новых задачах\n")
            logger.log_message("error")
        elif user_password != "boss" and user_password != "worker":
            print("Введен неправильный пароль\n")
            logger.log_message("critical")

def view_tasks():
    """Функция по просмотру сведений о текущих рабочих задачах в базе данных"""
    dict_tasks = {
        "boss": "руководитель",
        "worker": "сотрудник"
    }
    user_password = str(input("Введите пароль: "))
    if user_password == "boss":
        user_choice = str(input("Если вы хотите просмотреть данные обо всех сотрудниках, нажмите 1\n"
                                "Если вы хотите просмотреть данные о конкретном сотруднике, нажмите 2\n"))
        if user_choice == "1":
            with open("tasks.txt", "r") as file:
                if user_choice == "1":
                    for line in file:
                        print(line)
                elif user_choice == "2":
                    worker_info = str(input("Введите данные сотрудника для поиска: "))
                    for line in file:
                        if worker_info.lower() in line.lower():
                            print(line)
                elif user_choice != "1" and user_choice != "2":
                    while user_choice != "1" and user_choice != "2":
                        user_choice = str(input("Вы ввели неправильное число. Попробуйте снова:\n"))
                        logger.log_message("warning")
    if user_password == "worker":
        with open("tasks.txt", "r") as file:
            info_worker = str(input("Введите вашу фамилию для поиска: "))
            for line in file:
                if info_worker.lower() in line.lower():
                    print(line)
    if user_password not in dict_tasks:
        print("Вы ввели неправильный пароль\n")
        logger.log_message("critical")
