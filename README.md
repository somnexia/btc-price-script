# Bitcoin Price Tracker

Учебный Python-проект для задания по разработке, размещению и мониторингу:

- получает актуальную цену Bitcoin из публичного API CoinGecko;
- отправляет сообщение в Discord через Webhook;
- сохраняет цену в MySQL;
- пишет структурированные логи в stdout для Coolify/Grafana/Loki;
- хранит секреты только в переменных окружения.

## Структура

```text
src/main.py         # основной запуск
src/config.py       # настройки из environment variables
src/service.py      # запрос к API и отправка в Discord
src/repository.py   # таблица MySQL и запись цены
src/database.py     # подключение к MySQL
schema.sql          # схема таблицы для phpMyAdmin
.env.example        # пример переменных без настоящих секретов
```

## Переменные окружения

Скопируйте пример и заполните значения:

```bash
cp .env.example .env
```

Главные переменные:

- `DISCORD_WEBHOOK` - Discord Webhook URL.
- `DB_HOST` - имя MySQL-сервиса в Coolify.
- `DB_PORT` - обычно `3306`.
- `DB_NAME` - имя базы данных.
- `DB_USER` - пользователь MySQL.
- `DB_PASSWORD` - пароль MySQL.

Настоящий `.env` не должен попадать в GitHub.

## Локальный запуск

```bash
pip install -r requirements.txt
set -a
source .env
set +a
python src/main.py
```

## MySQL/phpMyAdmin

Скрипт сам создает таблицу `btc_prices`, если ее еще нет. Если хотите создать ее вручную через phpMyAdmin, импортируйте `schema.sql`.

Поля таблицы:

- `id` - автоинкрементный идентификатор;
- `price` - цена BTC;
- `currency` - валюта, по умолчанию `eur`;
- `fetched_at` - время записи.

## Coolify

1. Подключите публичный GitHub-репозиторий как Application.
2. В разделе Environment Variables добавьте значения из `.env.example`.
3. Для регулярного запуска используйте Scheduled Task:
   - Command: `python src/main.py`
   - Cron: например `*/30 * * * *` для запуска каждые 30 минут.
4. Убедитесь, что приложение и MySQL находятся в одной сети Coolify, а `DB_HOST` равен имени MySQL-сервиса.

## Логи для Grafana/Loki

Примеры строк:

```text
[INFO] service=btc-bot event=run_started message="Cron job started"
[INFO] service=btc-bot event=price_fetched price=60000 currency=eur message="BTC: 60000 EUR"
[INFO] service=btc-bot event=db_saved price=60000 currency=eur message="Saved to MySQL"
[INFO] service=btc-bot event=discord_sent message="Sent to Discord"
[ERROR] service=btc-bot event=run_failed message="..."
```

Примеры LogQL:

```logql
{app="btc-bot"}
{app="btc-bot"} |= "[ERROR]"
count_over_time({app="btc-bot"} |= "Sent to Discord" [1h])
```

## Безопасность

Если настоящий Discord Webhook или пароль MySQL уже был опубликован в GitHub, его нужно заменить: удалить из кода недостаточно, потому что секрет остается в истории Git.
