# Социальная сеть: пользователи и посты

Данное приложение позволяет создавать пользователей и публиковать посты от их имени в формате JSON.

---

### Технологии
Django 4, Django REST Framework 3.13, Docker, PostgreSQL


### Описание
Функции приложения:
- регистрация пользователя
- авторизация пользователя (получить токен)
- обновление токена пользователя
- создание, редактирование, удаление (CRUD) постов
- вывод постов списком
- пагинация постов
- фильтрация постов по параметрам запроса


#### Замечания:
- Пост может создать только зарегистрированный пользователь (автор).
- Любой авторизованный пользователь может просматривать посты других пользователей.
- Пользователь может обновлять / удалять только свои посты.
- У поста может быть несколько изображений.


### Локальный запуск приложения
#### Чтобы поднять контейнеры
```bash
docker stop $(docker ps -aq)
docker-compose -f infra/docker-compose.yml -up --build
docker-compose exec -f infra/docker-compose.yml backend manage.py migrate
```

#### Чтобы добавить в базу тестовые данные
```bash
docker compose cp data/dump.json backend:/
docker-compose exec -f infra/docker-compose.yml backend manage.py loaddata /dump.json
```

#### Чтобы зайти внутрь контейнера бекенда
```bash
docker-compose exec backend sh
```

Сервис доступен по ссылке: [http://localhost:80/api/](http://localhost:8000/admin/)

Документация: [http://localhost:80/api/docs/](http://localhost:8000/admin/)

Админка: [http://localhost:80/admin/](http://localhost:8000/admin/)

----


#### Авторы
[Илья Боюр](https://github.com/IlyaBoyur)