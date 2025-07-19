# Сервис для работы с API proxy.family

![Фото интерфейса](https://private-user-images.githubusercontent.com/199893874/467579252-e51b7234-6834-464a-ae29-c530e7ca701a.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI4MjExNjYsIm5iZiI6MTc1MjgyMDg2NiwicGF0aCI6Ii8xOTk4OTM4NzQvNDY3NTc5MjUyLWU1MWI3MjM0LTY4MzQtNDY0YS1hZTI5LWM1MzBlN2NhNzAxYS5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxOFQwNjQxMDZaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04OGNkNjliZGQ4ZTNkMDY4YmM3NDI5MGYxNzdiZTQwYzliOTFiYjM2YTNhY2E1ZmJjNzFmMTJmNjZmZTNlMmYzJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.xJeii3qG0lOztPcNY2YmCC5uIuKcQ03l77ug8bNUSHY)

Управление вашим кабинетом прямо из терминала

# Краткое описание

Сервис подключается и работает с api сайта proxy.family

- Вывод email пользователя и его баланс
- Покупка, парсинг и вывод списка прокси

# Установка (инструкция)

#### Для работы программы вам понадобятся:

- python
- git (по желанию)

Сначала устанавливаем [python](https://www.python.org/downloads/) на ваше устройство, советую версию 3.10. Следуйте инструкциям сетапа, не забудьте активировать кнопку "добавить в PATH".

А скачать git можно [здесь](https://git-scm.com/downloads)

После того как вы выполнили предыдущие шаги, можно начинать загрузку приложения.

# Если вы установили git

Откройте терминал (командную строку) и введите команду:

``
git clone https://github.com/makfwet/proxy_family_api
cd proxy_family_api
``

Запускаем run.bat

# Если вы не устанавливали git:

Скачиваем репозиторий в виде архива, распаковываем.

![Инструкция по загрузке архива](https://github-production-user-asset-6210df.s3.amazonaws.com/199893874/468250475-aa743af9-4a64-40c5-a8ca-50e874a3ef97.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVCODYLSA53PQK4ZA%2F20250719%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250719T032706Z&X-Amz-Expires=300&X-Amz-Signature=e474304f77ac9a4b4689922c62d650ddce7c7719357de5d68e5a20f45e9775aa&X-Amz-SignedHeaders=host)

Запускаем run.bat

>В обоих случаях высветится ошибка, сообщающая об отсутствии api ключа.
> 
>Это нормально, для настройки апи ключа читайте следующую главу

# Первоначальная настройка

В общем-то ничего сложного. В файл config.txt добавить api ключ вашего аккаунта.

Получить ключ можно по [ссылке](https://www.proxy.family/profile/api) (Не забудьте войти в свой аккаунт proxy.family)
![Фото api ключа](https://private-user-images.githubusercontent.com/199893874/467584500-44cbcd63-9cd3-4425-9c28-51b0534c7f60.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI4MjExNDMsIm5iZiI6MTc1MjgyMDg0MywicGF0aCI6Ii8xOTk4OTM4NzQvNDY3NTg0NTAwLTQ0Y2JjZDYzLTljZDMtNDQyNS05YzI4LTUxYjA1MzRjN2Y2MC5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxOFQwNjQwNDNaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT0xNDFjMjI1MjEyNjBjZjMxOGZmNjczZTdjYzgxZjRhNDI5NDYyMzA0ZGQ3OTU1Njc0NmYzZTE3MTllN2VjM2E2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.LqMqRL4GjUZzJSo-i3aeFHsnRs8_GOI2qs3dRNghbSU)

>Копируйте ключ и вставляйте его в файл без кавычек!

Должно получится примерно так:

![Фото конфига](https://private-user-images.githubusercontent.com/199893874/467832912-80e3e128-0920-47e8-b93d-b0598afa59b4.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTI4MjEwOTgsIm5iZiI6MTc1MjgyMDc5OCwicGF0aCI6Ii8xOTk4OTM4NzQvNDY3ODMyOTEyLTgwZTNlMTI4LTA5MjAtNDdlOC1iOTNkLWIwNTk4YWZhNTliNC5qcGc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUwNzE4JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MDcxOFQwNjM5NThaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT05OGFhMzZlNmMwYWJhN2I4M2UxZTExMDY4ZmI4ZGJkN2E4YjJhZjUxOWZiMmFhNjRiZGI3NDVmOGE3ODRkN2M4JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.qYJf6F2OxaF0Js2iWtFXaJQA-lSh6eZIMLsGP_3_QhU)

 

# Начало работы

Для работы необходимо стабильное подключение к интернету. Запускаем run.bat

# Список планируемых новых функций для будущих обновлений

- Расширить функционал приложения путем добавления существующих api функций у сайта
- Запись купленных прокси в .xlsx эксель таблицу / .txt текстовый файл 
- Графический интерфейс
- Фикс багов