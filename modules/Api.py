import requests


#Получаем api ключ из конфига
file = open(".\config.txt", "r")
API_KEY = file.read()

if API_KEY == "":
    file.close()

    print("Api ключ отсутствует")
    input("Нажмите Enter для выхода...")
    exit()

file.close()


#Класс для работы с api сайта proxy.family
class Api:


    SITE = "https://www.proxy.family/api/"
    HEADERS = {
        "Api-Token": API_KEY,
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
         AppleWebKit/537.36 (KHTML, like Gecko) \
         Chrome/135.0.0.0 Safari/537.36",
        "Accept": "application/json",
        "Connection": "keep-alive",
    }


    #Метод для проверки подключения к сайту. Возвращает True/false
    @staticmethod
    def check_connection():
        try:
            requests.get(Api.SITE)
            return True
        except requests.exceptions.ConnectionError:
            print("Проверьте подключение к интернету")
            return False


    #Метод для отправки GET запроса. Возвращает тело ответа/ошибку
    @staticmethod
    def get_request(endpoint, params=None):
        try:
            return requests.get(Api.SITE + endpoint,
                                headers=Api.HEADERS, params=params)

        except Exception as e:
            return e


    #Метод для отправки POST запроса. Возвращает тело ответа/ошибку
    @staticmethod
    def post_request(info, data):
        try:
            return requests.post(Api.SITE + info,
                                 headers=Api.HEADERS, data=data)

        except Exception as e:
            return e


    @staticmethod
    def proxy_list(amount):
        """
        GET метод для получения указанного количества прокси.
        Выводит строки-прокси в терминал построчно или возвращает ошибку.
        Требует указания количества выводимых прокси в параметр amount
        В противном случае возвращает ошибку
        """

        params = {
            "tariff_id": 5,
            "sort": "DESC",
            "limit": amount
        }

        try:
            get_proxy_list = Api.get_request("proxy/list", params)
            data_proxies_json = get_proxy_list.json()['data']['proxies']

            founded_proxies = []


            # Цикл парсит строки ip:port:login:password из json
            for i in data_proxies_json:
                proxy_data = data_proxies_json[i]

                proxy_string = (f"{proxy_data['ip']}:"
                          f"{proxy_data['http_port']}:"
                          f"{proxy_data['login']}:"
                          f"{proxy_data['password']}")

                founded_proxies.append(proxy_string)


            for i in founded_proxies:
                print(i)


        except Exception as e:
            return e


    @staticmethod
    def user_info():
        """
        GET метод для получения информации о пользователе.
        Выводит баланс и почту, к которой привязан аккаунт
        В противном случае выводит ошибку
        """

        try:
            get_user_info = Api.get_request("user/info")
            user_info_json = get_user_info.json()

            print(
                f"Ваш баланс: {user_info_json['data']['user']['balance']}"
                f"руб \n"
                f"{user_info_json['data']['user']['email']} \n"
            )

        except Exception as e:
            print(f"Ошибка метода user_info: {e}\n"
            f"Скорее всего, по причине плохого соединения с интернетом")


    @staticmethod
    def order_create(amount):
        """
        POST метод для покупки прокси IPV4 на 30 дней
        Требует указания количества покупаемых прокси в параметр amount
        В противном случае выводит ошибку
        """

        params = {
            "tariff_id": "5",
            "term_days": "30",
            "count": amount
        }

        try:
            Api.post_request("order/create", params)

        except Exception as e:
            print(f"Ошибка метода order_create: {e}")