# Телеграм Бот - Студенческий Проект

## Описание
Этот телеграм-бот предназначен для запроса публичных данных Центра банка и их отображения на экране. Он также настроен для работы с базой данных.

## Документация
    [Документация](https://danilachekmarev.github.io/SparkInTheDark_bot/) При помощи Doxygen лежит в /docs
    https://danilachekmarev.github.io/SparkInTheDark_bot/

## Установка

Для установки необходимых зависимостей выполните следующие шаги:

1. Убедитесь, что у вас установлен Python 3.7 или выше.
2. Клонируйте репозиторий
3. Установите необходимые библиотеки:
```
pip install -r requirements.txt
```
4. Создайте файл .env в корне проекта и добавьте токен вашего бота:
```
BOTTOKEN = <ваштокен_бота>
```
## Запуск
Чтобы запустить бота, выполните следующую команду:
```
python main.py
```
## Функциональность

- **Запрос данных Центра банка**: Бот может запрашивать и отображать актуальные данные о валютах.
- **Работа с базой данных**: Бот может сохранять данные в базе данных и извлекать их по запросу.

## Использование

Для начала работы Напишите боту в телеграме /start
[@SparkInTheDark_bot](https://telegram.me/SparkInTheDark_bot)

## Лицензия

Этот проект лицензирован под MIT License.