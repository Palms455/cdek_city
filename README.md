# cdek_city
1. Скрипт для внесения в PgSQL данных из файлов .ods

db_settings.py- настройки БД
db_update.py - инициализация

Зависимости: 
peewee==3.13.1
psycopg2==2.8.4
pyexcel-ods3==0.5.3

Найстройки бд db_settings.py
Именование классов так как прописано в PgSQL
Файлы .ods необходимо поместить в ту же директорию со скриптом

2. API для отображения спика городов. /api/
Реализована постраничная пагинация. 