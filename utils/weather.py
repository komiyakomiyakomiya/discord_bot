import datetime
import json
import os
import requests


class OpenWeather(object):
    def __init__(self):
        # APIキーの指定
        self.API_KEY = os.environ.get('OPEN_WEATHER_MAP_API_KEY')
        self.city = "Tokyo,JP"
        # APIのひな型
        self.api = "http://api.openweathermap.org/data/2.5/forecast?lang=ja&units=metric&q={city}&APPID={key}"

        # APIのURLを得る
        url = self.api.format(city=self.city, key=self.API_KEY)
        # 実際にAPIにリクエストを送信して結果を取得する
        req = requests.get(url)
        # 結果はJSON形式なのでデコードする
        self.data = json.loads(req.text)

    def get_city(self):
        return self.data['city']["name"]

    def get_weather(self, is_5days=False):
        # 今日の日付
        date_today = datetime.date.today()
        wether_text = ''
        for item in self.data["list"]:
            timestamp = item['dt_txt']

            # is_5daysフラグがFalseのときは
            if is_5days is False:
                # タイムスタンプに今日の日付が含まれていなければcontinue
                if str(date_today) not in timestamp:
                    continue

            date = datetime.datetime.strptime(
                timestamp, '%Y-%m-%d %H:%M:%S').strftime('%m/%d %H:%M')
            weather = item['weather'][0]["description"]
            temp = item["main"]["temp"]
            wether_text += f'> {date} {weather} {temp}℃\n'
        return wether_text
