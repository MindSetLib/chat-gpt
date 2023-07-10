import requests
import openai
from config import Config

openai.api_key = Config.API_KEY


async def make_requests(question: str):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + Config.API_KEY,
        'OpenAI-Organization': Config.ORGANIZATION_ID,
    }

    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {
                'role': 'user',
                'content': question,
            },
        ],
        'temperature': 0.7,
    }

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=json_data)
    return response.json()['choices'][0]['message']['content']


async def make_request_openai(question: str):
    system_msg = 'You are a helpful assistant for developers.'

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": system_msg},
                                                      {"role": "user", "content": question}])

    return response["choices"][0]["message"]["content"]
