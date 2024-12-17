#!/usr/bin/env python3
"""! @brief Обработака команды /get."""

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
     
def get_from_db(username: str):
    """!
    @brief Получает Сообщение пользователя из базы данных по имени пользователя.

    Эта функция выполняет SQL-запрос для получения Сообщения пользователя из таблицы
    user_values_table по указанному имени пользователя. Если пользователь найден, возвращается
    его значение. В противном случае возвращается сообщение о том, что пользователь не оставлял сообщения.

    @param username Имя пользователя, чье значение нужно получить.
    
    @return Возвращает Сообщения пользователя, если оно существует, или сообщение об отсутствии записи.
    """

    cursor.execute('SELECT user_value FROM user_values_table WHERE username = ?;', (username,))
    res = cursor.fetchone()

    if res is not None:
        return res[0]  # Return the user_value
    else:
        return "Этот пользователь не оставлял сообщение"  # No match found

@router.message(Command("get"))
async def cmd_get(message: Message, command: CommandObject):
    """!
    @brief Обработчик команды /get.

    Эта функция обрабатывает команду /get, получает аргументы команды,
    извлекает Сообщение пользователя из базы данных и отправляет ответ пользователю.

    @param message Сообщение, полученное от пользователя, содержащие команду /get.
    @param command Имя пользователя у которого хотят узнать Сообщение.

    @note Если аргументы не переданы, пользователю будет отправлено сообщение об ошибке.
          Функция предполагает, что база данных и таблица уже созданы и доступны.
    """
    if command.args is None:
        await message.answer(
            "Ошибка: не переданы аргументы. Пример:\n"
            "/get <username>"
        )
        return

    username = command.args
    user_value = get_from_db(username)

    await message.answer(
        f'Сообщение от {username}:\n'
        f"{user_value}"
    )