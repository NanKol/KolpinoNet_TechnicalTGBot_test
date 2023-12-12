
# Ставим бота на сервер
## Установка Git и скачиванием бота(можно обойтись sftp)

Проверяем утсановлен ли git

```bash
  git --version
```

Устанавливаем

```bash
  apt install git
```

Перехоим в директорию где будет бот и клонируем его

```bash
git clone https://github.com/NanKol/KolpinoNet_TechnicalTGBot.git
```

## Установка Pyhton и вирутального окружения

### Установка питона
Проверяем установлен ли Pyhton(как правило он уже стоит)

```bash
  python3 --version
```

Нам нужна версия 3.8+, если версия ниже, то ставим нужный.
Тестировался на 3.10

```bash
  тут сложнее
```

### создаём виртуальное окружение
Переходим в папку бота и создаём виртуальное окружение 
```bash
  python3 -m venv venv
```

Еслт стояла версия python ниже необходимой, то указываем нужную версию
```bash
  python3.10 -m venv venv
```
Если выдаёт ошибку то используем 
```bash
sudo apt install python3.10-venv
```

активируем виртуальное окружение
```bash
  source venv/bin/activate
```
Слева должны были появиться скопки (venv)

### Установка зависимостей
Устанавливаем зависимости
```bash
pip install -r requirements.txt
```

если выдаёт ошибку
```bash
sudo apt install python3-pip
```

## Редактируем конфиги
Редактируем файл с конфигами config.ini зарание или с помощью nano. 
Использовать только латиницу.
```bash
sudo nano config.ini
```

## Запуск бота с помощью Systemd

В директории 
```
/etc/systemd/system
```
Создаём файл
```bash
sudo nano KolpinoNet_TechnicalTGBot.service
```
и заполняем 
```bash
[Unit]
Description=<KolpinoNet_TechnicalTGBot>
After=syslog.target
After=network.target

[Service]
Type=simple
User=<Юзер от которого будет запускаться>
WorkingDirectory=<директория бота /home/username/KolpinoNet_TechnicalTGBot>
ExecStart=</home/username/Python_TG_bot/venv/bin/python3 /home/username/KolpinoNet_TechnicalTGBot/main.py
Restart=always

[Install]
WantedBy=multi-user.target
```
Запускаем бота
```bash
sudo systemctl enable Python_TG_Bot
sudo systemctl start Python_TG_Bot
```

Перезагружаем systemd если не видет нами созданный файл
```bash
sudo systemctl daemon-reload
```
