r"""
    ## Модуль для роботи з API штучного інтелекту(OpenAI)
    ### у цьому файли генерувати відповіді від ШІ 
"""
import openai
import dotenv, os

# беремо токен штучного інтелекту для його створення 
dotenv.load_dotenv()
OPENAI_SECRETKEY = os.getenv("OPENAI_SECRETKEY")

# підгружає ШІ для клієнта 
client_openai = openai.AsyncOpenAI(api_key= OPENAI_SECRETKEY)

# асінхронна функція яка отримує відповідь 
async def get_responce_from_ai(request: str):
    # генерує текст за допомогою токенів
    response = await client_openai.chat.completions.create(
        model="gpt-4o-mini", # модель яку ми використовуємо 
        messages = [{
            "role": "user", # чию роль використомвуємо 
            "content": request, # який контент отримуємо 
        }]
    )
    #  генерує та повертає нам відповідь 
    return response.choices[0].message.content
        

