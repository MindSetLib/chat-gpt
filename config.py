import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    TOKEN = os.environ.get('TOKEN')
    API_KEY = os.environ.get('API_KEY')
    ANTHROPIC_API_KEY = os.environ.get('ANTHROPIC_API_KEY')
    PROXY_URL = os.environ.get('PROXY_URL')
    OPENAI_API_URL = "https://api.openai.com/v1/chat/completions"
