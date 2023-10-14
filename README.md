# ВТБ на карте

Сервис позволяющий найти рядом с вами оптимально отделение банка ВТБ, которое окажет вам необходимые услуги в короткий срок

# Установка серверной части
Для установки серверной части вам необходимо использовать Docker версии не ниже 20. Инструкцию по установке можете найти [здесь](https://docs.docker.com/engine/install/)

Далее вам следует заполнить файлы переменных окружений. Например, следующим образом:

***apps/api/.env***
```
DATABASE_URL=postgresql://user:password@pgsql/vtb
SECRET_KEY=NEPONATNIEBUKVIESLIUSEDAUTH
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
REFRESH_TOKEN_EXPIRE_MINUTES=360
```
***apps/pgsql/.env***
```
POSTGRES_USER=user
POSTGRES_PASSWORD=passwod
PGDATA=/data/
POSTGRES_DB=vtb
```
Для запуска тестовой среды:
```
docker compose -f docker-compose.dev.yml up -d --build
```
Для запуска продуктовой среды (only vtb.goodgenius.ru):
```
docker compose -d --build
```

# Android приложение

Последняя версия доступна в релизах github [main](https://github.com/gg-goodgenius/vtb/releases/tag/main)

Предыдущие версии можно наблюдать в [actions](https://github.com/gg-goodgenius/vtb/actions), в виде артефактов


