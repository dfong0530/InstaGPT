import requests
import json

def GetResponseFromChatGPT(api_key, message):

    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}',
    }

    body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": f"{message}"}]
    }

    body = json.dumps(body)

    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=body)

    response =  response.json()["choices"][0]["message"]["content"]

    if len(response) > 2000:
        response = response[:2000] + "..."

    return response