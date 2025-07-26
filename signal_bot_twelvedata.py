import logging
import time
import requests
from telegram import Bot


TOKEN = "8041021589:AAFuD-HElQI4yehKOJ328-V50XFhk9XQWfQ"
CHAT_ID = "2066686801"

bot = Bot(token=TOKEN)
logging.basicConfig(level=logging.INFO)

def fetch_signal():
    # Це місце для виклику логіки аналізу
    # Поки просто повертає тестовий сигнал
    return "🔔 Сигнал: Купувати EUR/USD (ймовірність > 90%)"

def main():
    while True:
        signal = fetch_signal()
        logging.info(f"Надсилаю сигнал: {signal}")
        bot.send_message(chat_id=CHAT_ID, text=signal)
        time.sleep(300)  # чекати 5 хвилин

if __name__ == "__main__":
    main()
