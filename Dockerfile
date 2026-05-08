FROM python:3.11-slim

# Устанавливаем cron
RUN apt-get update && apt-get install -y cron && rm -rf /var/lib/apt/lists/*

# Рабочая директория
WORKDIR /btc-price-script

# Сначала зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Копируем cron конфиг
COPY cronjob /etc/cron.d/btc-cron

# Выдаём права cron файлу
RUN chmod 0644 /etc/cron.d/btc-cron

# Регистрируем cron job
RUN crontab /etc/cron.d/btc-cron

# Создаём лог файл
RUN touch /var/log/cron.log

# Запускаем cron и выводим лог в stdout контейнера
CMD ["sh", "-c", "cron && tail -f /var/log/cron.log"]