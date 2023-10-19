# bewise.ai_test flask app project
### Описание 
Test task for bewaise.ai flask app
### Функционал
- Добавление в базу данных вопросов с помощью запроса на сервис https://jservice.io/api/random;
- Получение в ответ на запрос последнего сохраненного вопроса из БД;
### Запуск проекта
1. Клонировать репозиторий:
2. Перейти в папку с проектом:
3. Выполнить команду
```
sudo docker compose up
```
### Тестовый запрос
По адресу http://localhost:5000/questions отравить POST запрос вида {"questions_num": integer}.
### Для подключения к БД использовать:
```
Host: 127.0.0.1
Port: 5432
Usermane: postgres
Database: postgres
Password: postgres
```
### Автор проекта
Никита Шелепов
