# LINE Notify送信確認用モジュール

# -*- coding: utf-8 -*-
import requests
if __name__ == '__main__':
        # LINE Notifyのアクセストークンを入れる
        access_token = "****"
        url = "https://notify-api.line.me/api/notify"
        headers = {'Authorization': 'Bearer ' + access_token}
        message = "テスト"
        payload = {'message': message}
        requests.post(url, headers=headers, params=payload,)
