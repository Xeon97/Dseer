
from .. import loader, utils
import random

# Задаём список слов, которые будут выпадать случайно
WORDS = ["Баку", "Тру", "Комбат", "Былины", "Осо"]

@loader.tds
class RandomWordMod(loader.Module):
    """
    Модуль для вывода случайного слова из списка при использовании команды .bot
    """
    strings = {"name": "RandomWord"}

    async def botcmd(self, message):
        """
        .bot - вывод случайного слова
        """
        random_word = random.choice(WORDS)  # Выбираем случайное слово из списка
        chat_id = utils.get_chat_id(message)  # Определяем ID текущего чата
        await message.client.send_message(chat_id, random_word)  # Отправляем сообщение в текущий чат
