import os

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    TOKEN = os.environ.get('TOKEN')
    API_KEY = os.environ.get('API_KEY')
    ORGANIZATION_ID = os.environ.get('ORGANIZATION_ID')
