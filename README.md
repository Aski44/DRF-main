LMS-система, в которой каждый желающий может размещать свои полезные материалы или курсы.

DRF Project
Для запуска файла в Docker, ввести команду в терминал:
docker-compose up -d --build

Для работы с проектом необходимо:

Клонировать репозиторий: https://github.com/KateRomanova/DRF

Создать зависимости из файла pyproject.toml, выполнив команду <pip install> или <poetry install>

Заполнить свои данные в файл .env согласно списка из файла <env.sample>

Запустить Redis на ПК командой redis-server

Для запуска проекта наберите в терминале команду python manage.py runserver

Чтобы начать рассылку:

    В терминале запустите celery worker командой: <celery -A config worker -l INFO> (Для Windows: <celery -A config worker -l INFO -P eventlet>)

    В другом терминале запустите celery beat командой: <celery -A config beat -l info -S django>
Для запуска файла в Docker:

Ввести команду в терминал: docker-compose up -d --build