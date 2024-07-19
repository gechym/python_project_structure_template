from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()
import os

from utils.get_config import get_config

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
CONFIG = get_config()

class GeminiModel():
    def __init__(self) -> None:
        self._model = ChatGoogleGenerativeAI( #https://api.python.langchain.com/en/latest/chat_models/langchain_google_genai.chat_models.ChatGoogleGenerativeAI.html
            model = CONFIG['gemini_model_name'], 
            google_api_key = GOOGLE_API_KEY,
            temperature = 0.0,
        )
    def chat(self,user_input):
        return self._model.invoke(user_input).content