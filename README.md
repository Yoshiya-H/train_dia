# train_dia
電車のダイヤに乱れが発生しているかどうかをチェックしSlack通知します。
情報はYahoo! JAPAN 路線情報より取得。
python3.13にて動作確認。

## Lambda環境変数
MARUNOUCHI: https://transit.yahoo.co.jp/diainfo/133/0
SAIKYO_KAWAGOE: https://transit.yahoo.co.jp/diainfo/50/0
SHONAN_SHINJUKU: https://transit.yahoo.co.jp/diainfo/25/0
YOKOSUKA: https://transit.yahoo.co.jp/diainfo/29/0
SLACK_DEFAULT_CHANNEL: <Chnnel_ID>
SLACK_OAUTH_TOKEN: <OAuth_Token>

## layer
$ pip3 install requests -t ./layer/python
$ pip3 install beautifulsoup4 -t ./layer/python
$ cd ./layer/
$ zip -r9 ../train_dia_python_layer.zip .