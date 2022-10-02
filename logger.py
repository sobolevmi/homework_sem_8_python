from datetime import datetime


def log_time():
    """Функция по записи в журнал логов времени выполнения операции"""
    with open("log_magazine.txt", "a", encoding="utf8") as file:
        operation_time = datetime.now()
        file.write("Время выполнения операции: " + str(operation_time) + "\n")


def log_message(message):
    """Функция по записи в журнал логов сообщения о типе ошибки: WARNING (предупреждение) и CRITICAL (критическая ошибка)"""
    with open("log_magazine.txt", "a", encoding="utf8") as file:
        operation_time = datetime.now()
        if message == "warning":
            file.write("WARNING: введено число, выходящее за пределы диапазона\n")
        if message == "error":
            file.write("ERROR: у вводимого пароль пользователя отсутствуют права доступа\n")
        if message == "critical":
            file.write("CRITICAL: попытка несанкционированного доступа в систему\n")


def log_view():
    """Функция по выведению журнала логов в консоль"""
    with open("log_magazine.txt", "r", encoding="utf8") as file:
        for line in file:
            print(line)
