import discord
import os

from utils import weather


# 天気を取得するクラスのインスタンス作成
open_weather = weather.OpenWeather()
# Botの起動とDiscordサーバーへの接続
client = discord.Client()


# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    my_city = open_weather.get_city()
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return

    if message.content == '/w':
        result = open_weather.get_weather()
        await message.channel.send(f'我、今日のお天気をおしえてあげるものなり…。\n\n<{my_city}>\n{result}')

    if message.content == '/w5':
        result = open_weather.get_weather(is_5days=True)
        await message.channel.send(f'我、５日分のお天気をおしえてあげるものなり…。\n\n<{my_city}>\n{result}')

TOKEN = os.environ.get('DISCORD_BOT_TOKEN')
client.run(TOKEN)
