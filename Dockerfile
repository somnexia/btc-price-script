FROM python:3.11-slim

RUN apt-get update && apt-get install -y cron

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY cronjob /etc/cron.d/btc-cron
RUN chmod 0644 /etc/cron.d/btc-cron
RUN crontab /etc/cron.d/btc-cron

RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log