# train_dia
電車のダイヤに乱れが発生しているかどうかをチェックしSlack通知します。<br>
情報はYahoo! JAPAN 路線情報より取得。<br>
python3.13にて動作確認。<br>

## Lambda環境変数
MARUNOUCHI: https://transit.yahoo.co.jp/diainfo/133/0<br>
SAIKYO_KAWAGOE: https://transit.yahoo.co.jp/diainfo/50/0<br>
SHONAN_SHINJUKU: https://transit.yahoo.co.jp/diainfo/25/0<br>
YOKOSUKA: https://transit.yahoo.co.jp/diainfo/29/0<br>
SLACK_DEFAULT_CHANNEL: <Chnnel_ID><br>
SLACK_OAUTH_TOKEN: <OAuth_Token><br>

## layer

```
$ pip3 install requests -t ./layer/python
$ pip3 install beautifulsoup4 -t ./layer/python
$ cd ./layer/
$ zip -r9 ../train_dia_python_layer.zip .
```