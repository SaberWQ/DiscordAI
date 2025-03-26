r"""
    ## Модуль для роботи з Discord ботом
    ### У цьому файлі прописується логіка взаємодії бота(WorldIT_Helper) з сервером
"""
import discord, dotenv, os

# тут з файлу .env  отримуємо токен 
dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

# ініцілізуємо бібліотеку 
intents = discord.Intents.default()
intents.message_content = True

# робимо бота діскорд на бозові налаштування 
bot = discord.Client(intents=intents)

# декоратор івент та базова функція 
@bot.event
async def on_ready():
    print("Бот запущенно")


@bot.event
# асинхронна функція для отримання повідомлення від серверу 
async def on_message(message):
    # умова яка перевіряє від кого це повідомлення 
    if message.author != bot.user:
        #  зберігає контент юзера 
        content = message.content
        # умова яка перевіряє контент 
        if content:
            #  надсилає той самий контент юзеру
            await message.channel.send(content)