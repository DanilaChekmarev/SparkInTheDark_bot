#!/usr/bin/env python3
"""! @brief Для безопасной работы с токеном телеграм бота."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

class Settings(BaseSettings):
    """!
    @brief Класс для управления настройками приложения. 

    Этот класс наследует от BaseSettings и используется для загрузки конфигурации
    из файла окружения. В .env токен бота, необходимый для работы приложения.
    """

    # Желательно вместо str использовать SecretStr 
    # для конфиденциальных данных, например, токена бота
    bot_token: SecretStr

    # Указывает файл окружения .env с токеном бота
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')

# При импорте файла сразу создастся 
# и провалидируется объект конфига, 
# который можно далее импортировать из разных мест
config = Settings()