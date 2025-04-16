import json
import requests
from bs4 import BeautifulSoup

SHONAN_SHINJUKU = 'https://transit.yahoo.co.jp/diainfo/25/0'
SAIKYO_KAWAGOE = 'https://transit.yahoo.co.jp/diainfo/50/0'
YOKOSUKA = 'https://transit.yahoo.co.jp/diainfo/29/0'
MARUNOUCHI = 'https://transit.yahoo.co.jp/diainfo/133/0'

dia_url_list = [ SHONAN_SHINJUKU, SAIKYO_KAWAGOE, YOKOSUKA, MARUNOUCHI ]

SLACK_URL = "https://slack.com/api/chat.postMessage"

with open('./auth.json', 'r', encoding="utf-8") as f:
    auth_settings = json.load(f)
# auth_settings = json.load(open('auth.json', 'r'))
slack_oauth_token = auth_settings["SLACK_OAUTH_TOKEN"]

headers = {
    "Authorization": f"Bearer {slack_oauth_token}",
    "Content-type": "application/json"
}

for url in dia_url_list:
    # HTMLの取得(GET)
    req = requests.get(url, timeout=10)

    # HTMLの解析
    soup = BeautifulSoup(req.text,"html.parser")

    # 要素の抽出
    head = soup.find("head")
    description = head.find("meta", property="og:description")
    title = head.find("meta", property="og:title")

    # 遅延情報があった場合のみ表示
    if description:
        description_content = description['content']
        titel_content = title['content']
        line_name = titel_content.split()
        if "に関する情報はありません" not in description_content:
            data = {
                "channel": "#info-train",
                "text": f":train:{line_name[0]}\n {description_content}"
            }
            response = requests.post(SLACK_URL, headers=headers, data=json.dumps(data), timeout=10)

            if response.status_code != 200:
                print(f"Slack通知失敗: {response.status_code}, {response.text}")
