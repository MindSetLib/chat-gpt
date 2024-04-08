import aiohttp
from aiohttp import ClientConnectorError
from openai.error import RateLimitError

from config import Config


async def make_model_request(question: str, model: str):
    answer = 'Не удалось получить ответ.'
    if model == 'gpt':
        answer = await make_gpt_request(question)
    elif model == 'claude':
        answer = await make_claude_request(question)
    return answer


async def make_gpt_request(question: str):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Config.API_KEY}"
    }

    json_data = {
        'model': 'gpt-3.5-turbo',
        'messages': [
            {'role': 'system', 'content': ''},
            {'role': 'user', 'content': question},
        ],
        'temperature': 0.5,
        'max_tokens': 500
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(Config.OPENAI_API_URL,
                                    headers=headers,
                                    json=json_data,
                                    proxy=Config.PROXY_URL) as response:

                if response.status == 200:
                    result = await response.json()
                    return result['choices'][0]['message']['content'].replace('\"', '')
                elif response.status == 403:
                    return 'Proxy error'
                else:
                    return 'Invalid api key'
        except RateLimitError:
            return 'Пополните кошелек'
        except ClientConnectorError:
            return 'API GPT не отвечает'


async def make_claude_request(question: str):
    url = "https://api.anthropic.com/v1/messages"

    headers = {
        "x-api-key": Config.ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json"
    }

    data = {
        "model": "claude-3-opus-20240229",
        "max_tokens": 1024,
        "messages": [
            {"role": "user", "content": question}
        ]
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data, proxy=Config.PROXY_URL) as response:
            if response.status == 200:
                response_json = await response.json()
                return response_json['content'][0]['text']
            else:
                error_message = f"Ошибка при запросе к модели Claude: {response.reason}"
                return error_message
