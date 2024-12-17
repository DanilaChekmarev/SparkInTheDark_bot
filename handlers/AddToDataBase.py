#!/usr/bin/env python3
"""! @brief Обработака команды /add."""

from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message
import sqlite3

##Для работы с Telegram API
router = Router()

## Установка соединения с базой данных SQLite
connection = sqlite3.connect('database/database.db', check_same_thread=False)

## Для работы с SQLite
cursor = connection.cursor()


def add_to_db(user_id: int, username: str, user_value: str):
    """!
    @brief Добавляет или обновляет Сообшение пользователя в базе данных.

    Эта функция выполняет вставку или обновление записи о пользователе в таблице
    user_values_table. Если пользователь с указанным user_id уже существует, его Сообшение
    будет обновлено.

    @param user_id Идентификатор пользователя.
    @param username Имя пользователя.
    @param user_value Сообщение, которое нужно сохранить для пользователя.
    
    @note Используется SQL-запрос с ON CONFLICT для обновления существующей записи.
    """

    cursor.execute('INSERT INTO user_values_table (user_id, username, user_value) VALUES (?, ?, ?) ON CONFLICT (user_id) DO UPDATE SET user_value = EXCLUDED.user_value;', (user_id, username, user_value))
    connection.commit()


@router.message(Command("add"))
async def cmd_add(message: Message, command: CommandObject):
    """!
    @brief Обработчик команды /add.

    Эта функция обрабатывает команду /add, получает аргументы команды,
    добавляет или обновляет значение пользователя в базе данных и отправляет ответ
    пользователю.

    @param message Сообщение, полученное от пользователя, содержащие команду /add.
    @param command Сообщение которое хочет доюавить пользователь.

    @note Если аргументы не переданы, пользователю будет отправлено сообщение об ошибке.
          Функция предполагает, что база данных и таблица уже созданы и доступны.
    """
    # Ошибка если плдьзователь не передал данные
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы. Пример:\n"
            "/add <message>"
        )
        return

    # Из класса message берём все необходимые аргументы
    new_user_id = message.from_user.id
    new_username = message.from_user.username
    new_user_value = command.args
    # Запись в дата-базу
    add_to_db(user_id=new_user_id, username=new_username, user_value=new_user_value)

    # Сообщение пользователю
    await message.answer(
        f'Добавлено в базу данных!\n'
        f"ID: {new_user_id}\n"
        f"username: {new_username}\n"
        f"Ваше сообщение: {new_user_value}\n"
    )