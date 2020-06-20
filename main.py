#Novel Translator via papago (JP -> KR)

from requests import Request
from requests import Session

f = open("novel.txt", encoding='UTF8')
text = f.read()
f.close()

s = Session()

headers = {
    'X-Naver-Client-Id': 'a',
    'X-Naver-Client-Secret': 'a',
}

payload = {
    'source': 'jp',
    'target': 'ko',
    'text': 'text'
}

url = 'https://openapi.naver.com/v1/language/translate'

req = Request('POST', url, data=payload, headers=headers)
prepped = req.prepare()

res = s.send(prepped)

result = res.json()['message']['result']['translatedText']

print(result)