import employees
import tasks
import salary
import logger
import export_data

def click_button():
    """Функция по запуску программы"""
    while True:
        choice_menu = str(input("Информационная система для работы с сотрудниками компании\n"
                       "Если вы хотите зайти в базу данных сотрудников компании, нажмите 1\n"
                       "Если вы хотите зайти в базу данных текущих задач сотрудников, нажмите 2\n"
                       "Если вы хотите зайти в базу данных сведений о текущей заработной плате, нажмите 3\n"
                       "Если вы хотите просмотреть список логов системы, нажмите 4\n"
                       "Если вы хотите экспортировать данные, нажмите 5\n"
                       "Если вы хотите завершить работу с системой, нажмите 'q'\n"))
        if choice_menu == "1":
            choice_menu_employees = str(input("Если вы хотите добавить данные о сотрудниках, нажмите 1\n"
                                              "Если вы хотите просмотреть базу данных сотрудников, нажмите 2\n"))
            if choice_menu_employees == "1":
                employees.add_employees()
                logger.log_time()
            if choice_menu_employees == "2":
                employees.view_employees()
                logger.log_time()
        elif choice_menu == "2":
            choice_menu_tasks = str(input("Если вы хотите добавить новые задачи, нажмите 1\n"
                                              "Если вы хотите просмотреть текущие задачи, нажмите 2\n"))
            if choice_menu_tasks == "1":
                tasks.add_tasks()
                logger.log_time()
            if choice_menu_tasks == "2":
                tasks.view_tasks()
                logger.log_time()
        elif choice_menu == "3":
            choice_menu_salary = str(input("Если вы хотите добавить новые данные о заработной плате, нажмите 1\n"
                                          "Если вы хотите просмотреть текущую базу данных заработной платы, нажмите 2\n"))
            if choice_menu_salary == "1":
                salary.add_employees_salary()
                logger.log_time()
            if choice_menu_salary == "2":
                salary.view_salary()
                logger.log_time()
        elif choice_menu == "4":
            logger.log_view()
            logger.log_time()
        elif choice_menu == "5":
            file_system_name = str(input("Введите наименование файла, данные в котором требуется экспортировать:\n"))
            export_data.export_data_from_file(file_system_name)
            logger.log_time()
        elif choice_menu == "q":
            break
        elif choice_menu != "1" and choice_menu != "2" and choice_menu != "3" and choice_menu != "4" and choice_menu != "q":
            while choice_menu != "1" and choice_menu != "2" and choice_menu != "3" and choice_menu != "4" and choice_menu != "q":
                choice_menu = str(input("Вы ввели неверное число. Попробуйте снова: \n"))
                logger.log_message("warning")
