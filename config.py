"""Модёль чтения конфига"""

import configparser

def get_config():
    config = configparser.ConfigParser()
    config.read("config.ini")
    
    return config


#TOKEN = 6434306263:AAH8JZtJCqSDp0zafl759UyGm5QqFLDvjpU

#ALL_TO_CHAT_ID = -1002050398431