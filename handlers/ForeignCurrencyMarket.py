#!/usr/bin/env python3
"""! @brief Обработака команды /ForeignCurrencyMarketData."""

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
import xmltodict
import requests

##Для работы с Telegram API
router = Router()

def combine_in_a_single_message(ForeignCurrencyMarketData):
    """!
    @brief Объединяет данные о валютном рынке в одно сообщение.

    Эта функция принимает данные о валютном рынке в формате словаря и формирует
    строку, содержащую дату и информацию о каждой валюте, включая название,
    стоимость, номинал и код.

    @param ForeignCurrencyMarketData Данные о валютном рынке в формате словаря,
                                     полученные из API центробанка.
    @return Строка, содержащая объединённую информацию о валютном рынке.

    @note На практике такой вывод в сообщение пользователю не удобный
    """
    single_message = ""
    single_message = f"{ForeignCurrencyMarketData['ValCurs']['@Date']}\n"
    for currency in ForeignCurrencyMarketData['ValCurs']['Valute']:
        single_message += currency['Name'] + "\t" + currency['Value'] + "\t" + currency['Nominal'] + "\t" + currency['CharCode'] + "\n"
    return single_message

@router.message(Command("ForeignCurrencyMarket"))
async def cmd_ForeignCurrencyMarket(message: Message):
    """!
    @brief Обработчик команды /ForeignCurrencyMarket.

    Эта асинхронная функция обрабатывает команду /ForeignCurrencyMarket, запрашивает
    данные о валютном рынке из API центробанка и отправляет пользователю
    котировки валют за последнюю зарегистрированную дату.
    """
    # api-endpoint
    URL = "https://www.cbr.ru/scripts/XML_daily.asp?"
    # Получаю .json
    response = requests.get(URL)
    # Использую xmltodict чтобы потом работать со словарем
    ForeignCurrencyMarketData = xmltodict.parse(response.content)
    # Из словаря делаю сообщение которое удобно выводится на экран
    ForeignCurrencyMarketTable = combine_in_a_single_message(ForeignCurrencyMarketData)

    await message.answer(
        (f"Котировки валют за последнюю зарегистрированную дату\n{ForeignCurrencyMarketTable}")
    )