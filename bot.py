#!/usr/bin/env python3
"""! @brief Главный файл из которого всё запускается."""
##
# @mainpage Телеграм бот студенческий проект
#
# @section description_main Описание
# Бот которорый Может запросить публичные данные центра банка и вывести их на экран.
# Так же настроен для работы с дата базой.
##


import asyncio
from aiogram import Bot, Dispatcher
from config_reader import config
from handlers import start, ForeignCurrencyMarket, AddToDataBase, GetFromDataBase

async def main():
    """!
    @brief Основная асинхронная функция для инициализации бота и запуска polling.

    Эта функция создает экземпляр бота с токеном, загружает маршруты из обработчиков,
    удаляет вебхук (если он установлен) и запускает процесс получения обновлений.
    
    @note Убедитесь, что токен бота правильно настроен в .env
    """

    # Для записей с типом Secret* необходимо 
    # вызывать метод get_secret_value(), 
    # чтобы получить настоящее содержимое вместо '*******'
    bot = Bot(token=config.bot_token.get_secret_value())
    
    dp = Dispatcher()

    # Подключение маршрутов обработчиков команд
    dp.include_router(start.router)
    dp.include_router(ForeignCurrencyMarket.router)
    dp.include_router(AddToDataBase.router)
    dp.include_router(GetFromDataBase.router)

    # Сброс ожидания обновлений, пока бот отключен
    await bot.delete_webhook(drop_pending_updates=True)

    # Запуск процесса получения обновлений от Telegram
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())