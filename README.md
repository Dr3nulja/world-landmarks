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
 
   ```json
   {
   "id": 1,
   "username": "user1",
   "email": "user1@example.com",
   "created_at": "2025-03-18T14:30:00Z"
   }
   ```
 - **POST** `/auth/login` – вход пользователя и получение JWT токена (Открытый)
 
    **Вход:**
    ```json
   {
     "email": "user1@example.com",
     "password": "password123"
   }
    ```
    **Выход:**
    **200 OK** – успешный вход
    ```json
   {
     "token": "JWT_TOKEN"
   }
    ```
    **401 Unauthorized** – неверные учетные данные
    ```json
   {
       "error": "Invalid credentials"
   }
   ```
   
     
   - **GET** `/auth/me` – получение информации о текущем пользователе (Авторизованный пользователь)
    **Вход:**
   
   *Данные не требуются, так как запрос будет использовать JWT токен для аутенфикации*
    
    **Выход:**
    **200 OK** – успешное получение информации о пользователе
    ```json
   {
     "id": 1,
     "username": "user1",
     "email": "user1@example.com",
     "created_at": "2025-03-18T14:30:00Z"
   }
    ```
    **401 Unauthorized** – Пользователь не авторизован или токен не предоставлен
    ```json
   {
       "error": "Invalid credentials"
   }
   ```
   
     ### Достопримечательности
     
    - **POST** /landmarks – добавление новой достопримечательности (Авторизованный пользователь)
     **Вход:**
    ```json
   {
     "name": "Statue of Liberty",
     "description": "A famous monument in New York",
     "location": "New York",
     "country": "USA",
     "imageUrl": "https://example.com/statue.jpg"
   }
    ```
    **Выход:**
    **201 Created** – успешное создание достопримечательности
    ```json
   {
     "id": 1,
     "name": "Statue of Liberty",
     "description": "A famous monument in New York",
     "location": "New York",
     "country": "USA",
     "imageUrl": "https://example.com/statue.jpg",
     "created_at": "2025-03-18T14:30:00Z",
     "user_id": 1
   }
    ```
    **400 Bad Request** – данные неверны или отсутствуют обязательные поля
    ```json
   {
     "error": "Missing required fields"
   }
   ```
   
    - **GET** /landmarks – получение списка всех достопримечательностей (Открытый)
      **Вход:**
      *Входные данные не требуются*
      **Выход:**
      **200 OK** – успешное получение списка достопримечательностей
      ```json
     {
         "id": 1,
         "name": "Statue of Liberty",
         "country": "USA",
         "location": "New York",
         "imageUrl": "https://example.com/statue.jpg"
       },
       {
         "id": 2,
         "name": "Eiffel Tower",
         "country": "France",
         "location": "Paris",
         "imageUrl": "https://example.com/eiffel.jpg"
       }
         ```
       
        - **GET** /landmarks/{id} – получение информации о конкретной достопримечательности (Открытый)
     **Вход:**
     *Входные данные не требуются*
     **Выход:**
     **200 OK** – успешный вход
     ```json
     {
       "id": 1,
       "name": "Statue of Liberty",
       "description": "A famous monument in New York",
       "location": "New York",
       "country": "USA",
       "imageUrl": "https://example.com/statue.jpg",
       "created_at": "2025-03-18T14:30:00Z"
     }

   ```
      **404 Not Found** – достопримечательность не найдена
      ```json
      {
       "error": "Landmark not found"
     }
      ```
       
      - **PUT** /landmarks/{id} – редактирование своей достопримечательности (Владелец)
       **Вход:**
      ```json
     {
       "name": "Statue of Liberty Updated",
       "description": "An updated description of the famous monument",
       "location": "New York",
       "country": "USA",
       "imageUrl": "https://example.com/updated_statue.jpg"
     }
      ```
      **Выход:**
      **200 OK** – успешное обновление
      ```json
     {
       "id": 1,
       "name": "Statue of Liberty Updated",
       "description": "An updated description of the famous monument",
       "location": "New York",
       "country": "USA",
       "imageUrl": "https://example.com/updated_statue.jpg",
       "updated_at": "2025-03-18T15:00:00Z"
     }
      ```
      **403 Forbidden** – пользователь не является владельцев достопримечательности
      ```json
     {
       "error": "Forbidden"
     }
     ```
       
      - **DELETE** /landmarks/{id} – удаление своей достопримечательности (Владелец)
       **Вход:**
     *Требуется только ID достопримечательности в URL*
      **Выход:**
      **200 OK** – успешное удаление
      ```json
     {
       "message": "Landmark deleted successfully"
     }
      ```
      **403 Forbidden** – пользователь не является владельцев достопримечательности
      ```json
     {
       "error": "Forbidden"
     }
     ```
       
      - **GET** /landmarks?country={country}&rating={rating} – фильтрация и сортировка по стране и рейтингу (Открытый)
       **Вход:**
      ```json
     {
       "country": "USA",
       "rating": 5
     }
      ```
      **Выход:**
      **200 OK** – успешная фильтрация и сортировка
      ```json
      {
         "id": 1,
         "name": "Statue of Liberty",
         "country": "USA",
         "location": "New York",
         "imageUrl": "https://example.com/statue.jpg"
       }
      ```

  ### Фотографии
 - **POST** /photos – загрузка новой фотографии для достопримечательности (Авторизованный пользователь)
       **Вход:**
      ```json
     {
       "landmark_id": 1,
       "imageUrl": "https://example.com/photo.jpg"
       }
      ```
      **Выход:**
      **201 Created** – успешная загрузка фотографии
      ```json
      {
       "id": 1,
       "landmark_id": 1,
       "imageUrl": "https://example.com/photo.jpg",
       "created_at": "2025-03-18T14:30:00Z"
     }
      ```
 - **GET** /photos?landmark_id={id} – получение списка фотографий для конкретной достопримечательности (Открытый)
          **Вход:**
      ```json
     {
       "country": "USA",
       "rating": 5
     }
      ```
      **Выход:**
      **200 OK** – успешная фильтрация и сортировка
      ```json
      {
         "id": 1,
         "name": "Statue of Liberty",
         "country": "USA",
         "location": "New York",
         "imageUrl": "https://example.com/statue.jpg"
       }
  - **PUT** /ratings/{id} – редактирование своей оценки (Владелец)
  - **DELETE** /ratings/{id} – удаление своей оценки (Владелец)




