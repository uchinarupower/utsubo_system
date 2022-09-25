# インストールした discord.py を読み込む
import discord
import utsubo_system

def get_token():
    with open("DISCORD_TOKEN.txt") as f:
        token = f.read()
    return token

def connect_discord():
    # 自分のBotのアクセストークンに置き換えてください
    TOKEN = get_token()

    # 接続に必要なオブジェクトを生成
    client = discord.Client()

    # 起動時に動作する処理
    @client.event
    async def on_ready():
        # 起動したらターミナルにログイン通知が表示される
        print(f'login to {client.user} !')
        #channel = client.get_channel(730244126481580075)
        #await channel.send('よろ^^')

    # 発言時に実行されるイベントハンドラを定義
    @client.event
    async def on_message(message):
        if message.author.bot:
            return

        if message.content.startswith('/us'):

            await message.channel.send('uoooooooo')



        #if message.content == "/neko":


    client.run(TOKEN)


def main():
    connect_discord()

main()