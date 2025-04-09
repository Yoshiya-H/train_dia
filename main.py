import requests
from bs4 import BeautifulSoup
from py2slack import send_slack

SHONAN_SHINJUKU = 'https://transit.yahoo.co.jp/diainfo/25/0'
SAIKYO_KAWAGOE = 'https://transit.yahoo.co.jp/diainfo/50/0'
YOKOSUKA = 'https://transit.yahoo.co.jp/diainfo/29/0'
MARUNOUCHI = 'https://transit.yahoo.co.jp/diainfo/133/0'

url_list = [ SHONAN_SHINJUKU, SAIKYO_KAWAGOE, YOKOSUKA, MARUNOUCHI ]

for url in url_list:
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
        if not "に関する情報はありません" in description_content:
            send_slack(line_name[0], ":", description_content)
