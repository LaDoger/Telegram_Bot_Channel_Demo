import os
import asyncio
import telegram
from dotenv import load_dotenv

async def main():
    load_dotenv()

    # Telegram Bot Token created from https://t.me/BotFather
    TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

    # Telegram Channel ID which is just "@" + your channel name
    CHANNEL_ID = os.getenv('CHANNEL_ID')
  
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)

    text = 'doge'

    await bot.send_message(chat_id=CHANNEL_ID, text=text)

if __name__ == '__main__':
    asyncio.run(main())