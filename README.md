# world-landmarks

## Описание проекта
> Веб-приложение для удобного управления мировыми достопримечательностями. Пользователи могут добавлять, удалять, редактировать достопримечательности, загружать фотографии и оставлять оценки. Для регистрации и аутентификации в приложении используется JWT.

## Команда проекта
- **Данис Низамов** – *Задачи участника*
- **Петр Харламов** – *Задачи участника*

## Используемые технологии
- **Язык программирования**: Python
- **Фреймворк**: Flask
- **Аутентификация**: JWT
- **База данных**: MySQL

## Основной функционал

### Пользователи
- Регистрация нового пользователя
- Аутентификация пользователя
- Получение информации о пользователе

### Достопримечательности
- Создание достопримечательности (доступно только для зарегистрированных пользователей)
- Получение списка всех достопримечательностей
- Получение информации о конкретной достопримечательности
- Управление (удаление и редактирование) только своих достопримечательностей

### Фотографии
- Загрузка новой фотографии к достопримечательности
- Получение списка фотографий конкретной достопримечательности
- Удаление только своих фотографий

### Оценки
- Добавление оценки к достопримечательности
- Получение средней оценки для конкретной достопримечательности
- Удаление и редактирование только своей оценки

### Фильтрация и сортировка
- Фильтрация достопримечательностей по стране
- Сортировка по рейтингу

## Установка и запуск
1. Скачать ZIP архив с проектом
2. Установить Python
3. Установить нужную базу данных (MySQL)
4. Настроить базу данных
5. Запустить приложение

## Описание эндпойнтов (Rest API)

### Аутентификация и регистрация пользователей

- **POST** `/auth/register` – регистрация нового пользователя (Открытый)
  
  **Вход:**
  ```json
  {
    "username": "user1",
    "email": "user1@example.com",
    "password": "password123"
  }
  ```
  **Выход:**
  **201 Created** – успешная регистрация

  **400 Bad Request** – если данные неверны (например, email уже зарегистрирован)

  **POST /auth/login** – вход пользователя и получение JWT токена (Открытый)

  **GET /auth/me** – получение информации о текущем пользователе (Авторизованный пользователь)
  
  ## Достопримечательности
  
  **POST /landmarks** – добавление новой достопримечательности (Авторизованный пользователь)

  **GET /landmarks** – получение списка всех достопримечательностей (Открытый)
  
  **GET /landmarks/{id}** – получение информации о конкретной достопримечательности (Открытый)
  
  **PUT /landmarks/{id}** – редактирование своей достопримечательности (Владелец)
  
  **DELETE /landmarks/{id}** – удаление своей достопримечательности (Владелец)
  
  **GET /landmarks?country={country}&rating={rating}** – фильтрация и сортировка по стране и рейтингу (Открытый)
