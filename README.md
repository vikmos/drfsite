### Сервер авторизации и новостей c комментариями
##### Стек
1. Django==4.1
2. djangorestframework==3.13.1
3. djangorestframework-simplejwt==4.8.0
4. gunicorn==20.1.0
5. environs==9.5.0
6. psycopg2-binary==2.9.3

##### Запуск приложения
1. Установить PostgreSQL, создать БД.
2. Клонировать репозиторий командой git clone https://github.com/vikmos/drfsite.git 
3. Перейти в каталог drfsite и активировать виртуальное окружение . /env/bin/activate
4. Установить необходимые для работы библиотеки командой pip install -r requirements.txt
5. Создать файл .env и заполнить его по примеру .env.example
6. В файле settings.py в директиве ALLOWED_HOSTS прописать адрес сервера
7. Выполнить:
    7.1 ~/drfsite/python manage.py makemigrations
        ~/drfsite/python manage.py migrate
    7.2 Создайте административного пользователя проекта с помощью следующей команды:
        ~/drfsite/manage.py createsuperuser
8. Настроить gunicorn:
    8.1 Скопировать файл /drfsite/config/gunicorn.socket в папку /etc/systemd/system/
    8.2 Скопировать файл /drfsite/config/gunicorn.service в папку /etc/systemd/system/
    8.3 Выполнить:
        8.3.1 sudo systemctl start gunicorn.socket
        8.3.2  sudo systemctl enable gunicorn.socket
        8.3.3 sudo systemctl status gunicorn
9. Настроить Nginx для Gunicorn:
    9.1 Скопировать файл /drfsite/config/drfsite в папку /etc/nginx/site-available/
    9.2 Выполнить:
        9.2.1 sudo ln -s /etc/nginx/sites-available/drfsite /etc/nginx/sites-enabled
        9.2.2 sudo nginx -t
        9.2.3 sudo systemctl restart nginx
        9.2.4 sudo ufw delete allow 8000
        9.2.5 sudo ufw allow 'Nginx Full'
Настройка окончена, сервер запущен.

##### Работа с сервером
Работа с сервером может производиться, как по средствам веб-интерфеса, так и по средствам консоли,
для этого нужно перейти по адресу http://51.250.51.137/
Установление пользователю прав адмнистратора, производится только из веб-интерфеса.
Просматривать список новостей и отдельную новость может любой авторизованный пользователь.
Добавлять новость может любой авторизованный пользователь.
Изменять и удалять новость может либо автор, либо администратор.

##### Роуты
**Регистрация новых пользователей:**
    **Веб-интрефейс** - http://51.250.51.137/api/v1/registr/
    **Djoser-токен** - ```curl -X POST http://51.250.51.137/api/v1/auth/users/ --data 'username=djoser&password=djoser'```

**Аутентификация пользователей:**
    **Веб-интрефейс** - http://51.250.51.137/api/v1/api-auth/login/
    **Djoser-токен** - ```curl -X POST http://51.250.51.137/api/v1/auth/token/login/ --data 'username=djoser&password=djoser'``` - для получения токена
    **Djoser-токен** - ```curl -X GET http://51.250.51.137/api/v1/auth/users/me/ -H 'Authorization: Token <token>'```
    **JWT-токен** - ```curl -X POST -H "Content-Type: application/json" -d '{"username": "davidattenborough", "password": "boatymcboatface"}' http://51.250.51.137/api/v1/token/``` - для получения токена
    **JWT-токен** - ```curl -H "Authorization: JWT <access-token>" http://51.250.51.137/api/v1/news/```
    
**Отключение от сервера**
    **Веб-интерфейс** - http://51.250.51.137/api/v1/api-auth/logout/
    **Djoser-токен** - ```curl -X POST http://51.250.51.137/api/v1/auth/token/logout/ -H 'Authorization: Token <token>'```
    
**Просмотр всех новостей**
    **Веб-интерфейс** - http://51.250.51.137/api/v1/news/
    **Djoser-токен** -``` curl -X POST http://51.250.51.137/api/v1/news/ -H 'Authorization: Token <token>'```
    **JWT-токен** - ```curl -H "Authorization: JWT <access-token>" http://51.250.51.137/api/v1/news/```

**Просмотр конкретной новости**
    **Веб-интерфейс** - ```http://51.250.51.137/api/v1/news/<ID новости>/```
    **Djoser-токен** - ```curl -X POST http://51.250.51.137/api/v1/news/<ID новости>/ -H 'Authorization: Token <token>'```
    **JWT-токен** - ```curl -H "Authorization: JWT <access-token>" http://51.250.51.137/api/v1/news/<ID новости>/```
    
**Добавление новости**
    **Djoser-токен** - ```curl -d '{"title":"some_title", "text":"some_text"}' -H "Content-Type: application/json" -H "Authorization: Token <token>" -X POST http://51.250.51.137/api/v1/news/```
    **JWT-токен** - ```curl -d '{"title":"some_title", "text":"some_text"}' -H "Content-Type: application/json" -H "Authorization: JWT <token>" -X POST http://51.250.51.137/api/v1/news/```
    
**Изменение новости**
    **Djoser-токен** - ```curl -d '{"title":"some_title", "text":"some_text"}' -H "Content-Type: application/json" -H "Authorization: Token <token>" -X PUT http://51.250.51.137/api/v1/news/<ID-новости>/```
    **JWT-токен** - ```curl -d '{"title":"some_title", "text":"some_text"}' -H "Content-Type: application/json" -H "Authorization: JWT <token>" -X PUT http://51.250.51.137/api/v1/news/<ID-новости>/```
    
**Удаление новости**
    **Djoser-токен** - ```curl -H "Authorization: Token <token>" -X DELETE http://51.250.51.137/api/v1/news/<ID-новости>/```
    **JWT-токен** - ```curl -H "Authorization: JWT <token>" -X DELETE http://51.250.51.137/api/v1/news/<ID-новости>/```
