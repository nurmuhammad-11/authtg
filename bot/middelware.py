
import asyncio
import logging
from aiogram import BaseMiddleware
from aiogram.types import Message

# Logger setup
logger = logging.getLogger("request_logger")
logging.basicConfig(filename="request_logs.log", level=logging.INFO, format="%(asctime)s - %(message)s")


# Aiogram Middleware
class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, limit: float):
        super().__init__()
        self.limit = limit
        self.last_time = {}  # Oddiy dict ishlatamiz # noqa

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        current_time = asyncio.get_running_loop().time()

        last_request_time = self.last_time.get(user_id, 0)

        if current_time - last_request_time < self.limit:
            await event.answer("Juda ko‘p so‘rov yubordingiz! ❗")  # noqa
            return  # Cancel qilish uchun None qaytaramiz # noqa

        self.last_time[user_id] = current_time
        return await handler(event, data)
