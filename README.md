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
Скачайте проект и перейдите в папку проекта.

#### Подготовьте переменные окружения для проекта:
```bash
cd infra
echo "SECRET_KEY=mysecretkey
DJANGO_DEBUG_VALUE=True
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres" > .env
```

#### Поднимите контейнеры и мигрируйте базу данных:
```bash
docker stop $(docker ps -aq)
docker-compose up --build -d
docker-compose exec backend python3 manage.py migrate
```

#### Добавьте в базу тестовые данные
```bash
docker compose cp ../data/dump.json backend:/
docker-compose exec backend python3 manage.py loaddata /dump.json
```

#### Профит! Чтобы зайти внутрь контейнера бекенда:
```bash
docker-compose exec backend bash
```

Сервис доступен по ссылке: [http://localhost:80/api/](http://localhost:8000/admin/)

Документация: [http://localhost:80/api/docs/](http://localhost:8000/admin/)

Админка: [http://localhost:80/admin/](http://localhost:8000/admin/)

(Логин: admin; пароль: admin)

----


#### Авторы
[Илья Боюр](https://github.com/IlyaBoyur)