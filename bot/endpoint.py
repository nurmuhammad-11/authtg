from requests import post, get
from config import AUTH_API, GET_USER


async def register_user(**kwargs):
    response = post(AUTH_API, data=kwargs)
    return response.status_code


async def get_user(telegram_id: int):
    response = get(f"{GET_USER}{telegram_id}")
    return response.status_code