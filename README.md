# TOP10MOVIES
Библиотека ваших любимых фильмов


## Как запустить проект

клонируем:
```
$ git clone https://github.com/lovelydaemon/top10movies
$ cd top10movies
```
создаем виртуальное окружение, активируем его и устанавливаем необходимые пакеты
из файла requirements.txt:
```
$ virtualenv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```
поиск фильмов происходит через API <http://www.omdbapi.com/>.
для работы с ним необходимо получить API KEY.

добавить файл .env в корневую папку проекта и прописать настройки:
```
SECRET_KEY='YOUR_SECRET_KEY'
DATABASE_URI='sqlite:///FILENAME.db'
MOVIE_API='API_KEY'
```
запуск проекта:
```
$ flask run
* Running on http://127.0.0.1:5000
```

## License
Лицензия MIT
