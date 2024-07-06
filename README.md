# Проект "Домашнее задание 11_1"

## Описание:

Проект "Домашнее задание 11_1" включает в себя следующие задания: создать инструменты для эффективной работы с 
большими объемами данных транзакций, используя возможности Python для обработки данных через генераторы

## Установка:

1. Клонируйте репозиторий:
```
git clone https://github.com/ValeriyaChulkovaa/myblog.git
```

2. Установите зависимости:
```
pip install -r requirements.txt
```


## Описание функций:

1. Функция filter_by_currency принимает на вход список словарей, представляющих транзакции.
2. Генератор transaction_descriptions принимает список словарей с транзакциями и возвращает описание 
каждой операции по очереди.
3. Генератор card_number_generator выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.


## Тесты:

1. Тест test_filter_by_currency_empty() проверяет функцию filter_by_currency()
2. Тест test_transaction_descriptions() проверяет функцию test_transaction_descriptions()
3. Тест test_card_number_generator() проверяет функцию card_number_generator()

## Запуск тестов терминал:
```
poetry run pytest --cov
```
