"""Хранится и генерируются сообщения бота"""
from aiogram.utils.formatting import Text, Bold

#Сообщения на команды /<команда>
start = """Бот запущен!\n
Используйте /help для просмотра команд бота"""

help = """Список команд бота:
        /start - Запускает бота
        /help - выводит информацию о доступных командах
        /menu - выводит меню
        /check - позоляет проверить исправна ли авария
Проверка аварии: \n/check <ip или TID> <XXX.XXX.XXX.XXX или XXX>"""
        
menu = """Меню:"""


#Осталные сообщения
count_trables = """На данный момент аварий: {count_trable}"""

no_trables = """Аварии не найдены."""

def about_trouble(emoji, trouble_id, adress, time_start, 
                  time, time_end:str,uzel, comment, brand,model, 
                  ipaddr,ecomment,count_fl,count_yl):
        
        pre_time_end = "Время конца: "
        if len(time_end) == 0:
                pre_time_end = ""
        
        text = Text(f"{emoji} Авария TID: {trouble_id}\n",
             Bold("Объект: "), f"{adress}\n",
             Bold("Время начала: "), f"{time_start}\n",
             Bold("Длительность: "), f"{time}\n",
             Bold(pre_time_end), f"{time_end}",
             Bold("Узел: "), f"{uzel}\n",
             Bold("Примечание: "), f"{comment}\n",
             Bold("Оборудование: "), f"{brand} {model} [{ipaddr}]\n",
             Bold("Коммент: "), f"{ecomment}\n",
             Bold("Кол-во ФЛ: "), f"{count_fl}\n",
             Bold("Кол-во ЮЛ: "), f"{count_yl}\n")
        
        return text