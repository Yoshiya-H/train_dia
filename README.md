# train_dia
電車のダイヤに乱れが発生しているかどうかをチェックしSlack通知します。<br>
情報はYahoo! JAPAN 路線情報より取得<br>

## Slack認証情報
### auth.json
# GitHub Secretsに認証情報を登録

```
{
    "SLACK_OAUTH_TOKEN": "<OAuth_Token>",
    "SLACK_DEFAULT_CHANNEL": "<Chnnel_ID>"
}
```