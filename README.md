## Финальный проект спринта: API для Yatube

Проект Yatube позволяет делиться пользователям новостями, событиями. Каждый желающий может вести свой блог и получать комментарии на свои сообщения. Есть возможность подписаться, если чьи-то посты наиболее интересны.

### API позволяет:
Просматривать все записи и комментарии к ним (для всех пользователей);
Создавать, редактировать, удалять свои записи (для зарегистрированных пользователей);
Создавать, редактировать, удалять свои комментарии к любым записям (для зарегистрированных пользователей);
Просмотреть свои подписки (для зарегистрированных пользователей);
Подписаться на ленту пользователя (для зарегистрированных пользователей).

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/NatalyaKozarezenko/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

### Примеры запросов:
1. Пример POST-запроса для пользователя Яндекс Практикум: добавление нового поста.
POST .../api/v1/posts/

```
{
    "text": "Учитесь в приложении Практикума когда и где хотите",
    "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAYABgAAD/4QBoRXhpZgAATU0AKgAAAAgABAEaAAUAAAABAAAAPgEbAAUAAAABAAAARgEoAAMAAAABAAMAAAExAAIAAAARAAAATgAAAAAAAJOjAAAD6AAAk6MAAAPocGFpbnQubmV0IDUuMC4xMwAA/9sAQwBQNzxGPDJQRkFGWlVQX3jIgnhubnj1r7mRyP///////////////////////////////////////////////////9sAQwFVWlp4aXjrgoLr/////////////////////////////////////////////////////////////////////////8AAEQgANAAxAwESAAIRAQMRAf/EAB8AAAEFAQEBAQEBAAAAAAAAAAABAgMEBQYHCAkKC//EALUQAAIBAwMCBAMFBQQEAAABfQECAwAEEQUSITFBBhNRYQcicRQygZGhCCNCscEVUtHwJDNicoIJChYXGBkaJSYnKCkqNDU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6g4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2drh4uPk5ebn6Onq8fLz9PX29/j5+v/EAB8BAAMBAQEBAQEBAQEAAAAAAAABAgMEBQYHCAkKC//EALURAAIBAgQEAwQHBQQEAAECdwABAgMRBAUhMQYSQVEHYXETIjKBCBRCkaGxwQkjM1LwFWJy0QoWJDThJfEXGBkaJicoKSo1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoKDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uLj5OXm5+jp6vLz9PX29/j5+v/aAAwDAQACEQMRAD8Au0UAFVpZSTtXp60my1BsnMir1YVUVGf7ozS5mVyJbstCVD/FUHkP6D86LsXLHuWetVVdo2x6dRRzA4di3TVYMuRVGbVh1FAEczbYz78Ulx/q/wAaT2LgtStRWZsWGPlwDbSRMHXy2FXutDJqzuwt2ZmOSTxSxLskYA54oQTs1oQP99vqaH++31NS9zRbEtu3zFfWm2/+s/CnEma0LVFWYjWXcpHrTqATsUiCpwetWpIw454PrUOJqp9yJWWOPIILGmtC46DNGqHo3dsWBgGYsevrTRE5/hoV0ErPqNfl2I9anjgA5bk+lFmw50hYE2rk9TUtUlYzlJsKKZIUUAFFABRQAUUAFFABRQAUUAf/2Q==",
    "group": 1
}
```
Пример ответа:
```
{
    "id": 4,
    "author": "yapraktikum",
    "image": "http://127.0.0.1:8000/media/posts/temp_ZXZS94p.jpeg",
    "text": "Учитесь в приложении Практикума когда и где хотите",
    "pub_date": "2024-10-26T12:56:37.999108Z",
    "group": 1
}
```
2. Пример GET-запроса gh для пользователя Nata: просмотр подписок.
GET .../api/v1/follow/
```
{
    "following": "yapraktikum"
}
```
Пример ответа:
```
[
    {
        "user": "Nata",
        "following": "yapraktikum"
    }
]
```