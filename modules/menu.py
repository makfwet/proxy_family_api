from time import sleep
from modules.Api import Api


def start_menu():
    """
    Функция - стартовое меню.
    Проверяет наличие подключения к сети.
    Бесконечно опрашивает пользователя пока тот не введет 1 или 2
    Если выбрано 1, то функция возвращает число 1
    Если выбрано 2, то функция завершает работу скрипта
    """
    check_connection_menu()

    while True:

        try:
            what_to_do = int(input(
            "1. Купить прокси" + "\n"
            "2. Выйти" + "\n"))

        except ValueError:
            continue

        if what_to_do != 1 and what_to_do != 2 and what_to_do != 3:
            continue

        elif what_to_do == 1:
            return what_to_do

        elif what_to_do == 2:
            exit()


#Функция - чекер подключения. Использует метод check_connection()
def checker():
    while True:

        for i in range(5):
            connection = Api.check_connection()


            if connection:
                return True

            sleep(2)


        return False


def check_connection_menu():
    """
    Функция - меню, объединяющая checker и консольный I/O
    Проверяет подключение к сети.
    Бесконечно опрашивает пользователя пока тот не введет 1 или 2
    Если выбрано 1, то функция снова проверяет подключение к сети
    Если выбрано 2, то функция завершает работу скрипта
    """

    while True:

        if checker():
            break

        while True:
            what_to_do = input(
                    f"Повторить попытку подключения?" + "\n"
                    "1. Да, повтори" + "\n"
                    "2. Нет, выходи" + "\n")


            if what_to_do != "1" and what_to_do != "2":
                continue

            break

        if what_to_do == "1":
            continue

        if what_to_do == "2":
            exit()


#Функция - меню для покупки, защита от некорректного количества прокси
def buying_menu():

    while True:

        try:
            amount = int(input("Введите количество прокси: "))

            if amount <= 0:
                continue

        except ValueError:
            continue

        break

    Api.order_create(amount)
    sleep(5)

    Api.proxy_list(amount)




def main():
    check_connection_menu()

    Api.user_info()
    print("Привет! Выбери действие:")

    while True:

        start_menu()
        buying_menu()
        Api.user_info()

        print("\n", "\n")