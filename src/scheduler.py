# scheduler.py

# Запускает main() каждые 300 секунд.
import time
from main import main
from config import INTERVAL

while True:
    main()
    time.sleep(INTERVAL)