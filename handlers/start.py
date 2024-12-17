#!/usr/bin/env python3
"""! @brief Обработака команды /start."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

##Для работы с Telegram API
router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):

    """!
    @brief Обработчик команды /start.

    Эта функция обрабатывает команду /start, отправляя пользователю
    приветственное сообщение с описанием доступных команд.
    
    @note Доступные команды:
          - /ForeignCurrencyMarket: Запрашивает публичный API центробанка котировок валют на сегодня и выводит их на экран.
          - /add <message>: Сохраняет сообщение от пользователя в Дата-базу. Пример использования: /add Это моё сообщение.
          - /get <username>: Выводит сообщение от пользователя из Дата-базы. Пример использования: /get danila_chekmarev.
    """

    await message.answer(
        "Привет!\n"
        "Мои команды:\n\n"
        "/ForeignCurrencyMarket\n"
        "Запрашивает публичный API центробанка котировок валют на сегодня и выводит их на экран\n\n"
        "/add <messege>\n"
        "Сохраняет сообщение от пользователя в Дата-базу\n"
        "Пример:\n"
        "/add Это моё сообщение\n\n"
        "/get <username>\n"
        "Выводит сообщение от пользователя из Дата-базы\n"
        "Пример:\n"
        "/get danila_chekmarev\n\n"
    )