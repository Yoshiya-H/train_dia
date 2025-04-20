import json
import os
import requests
from bs4 import BeautifulSoup

def lambda_handler(event, context):

    SHONAN_SHINJUKU = os.environ['SHONAN_SHINJUKU']
    SAIKYO_KAWAGOE = os.environ['SAIKYO_KAWAGOE']
    YOKOSUKA = os.environ['YOKOSUKA']
    MARUNOUCHI = os.environ['MARUNOUCHI']

    dia_url_list = [ SHONAN_SHINJUKU, SAIKYO_KAWAGOE, YOKOSUKA, MARUNOUCHI ]

    SLACK_URL = "https://slack.com/api/chat.postMessage"
    SLACK_OAUTH_TOKEN = os.environ['SLACK_OAUTH_TOKEN']

    headers = {
        "Authorization": f"Bearer {SLACK_OAUTH_TOKEN}",
        "Content-type": "application/json"
    }
    notifications = []

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
                notifications.append(f":train:{line_name[0]}\n {description_content}")
    if notifications:
        data = {
            "channel": "#info-train",
            "text": "\n\n".join(notifications)
        }
        response = requests.post(SLACK_URL, headers=headers, data=json.dumps(data), timeout=10)

        if response.status_code != 200:
            print(f"Slack通知失敗: {response.status_code}, {response.text}")
