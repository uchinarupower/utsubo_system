# インストールした discord.py を読み込む
import discord
import utsubo_system


def connect_discord():
    # 自分のBotのアクセストークンに置き換えてください
    TOKEN = 'MTAyMzUyOTE1OTUwNDQ0OTU0OA.GQfNvC.1ZZnrG2fcwaWLHeCFP8KiNoTH4KcatwsV8EBlM'

    # 接続に必要なオブジェクトを生成
    client = discord.Client()

    # 起動時に動作する処理
    @client.event
    async def on_ready():
        # 起動したらターミナルにログイン通知が表示される
        print(f'login to {client.user} !')
        channel = client.get_channel(730244126481580075)
        await channel.send('よろ^^')

    @client.event
    async def on_message(message):
        if message.author.bot:
            return


        if message.content.startswith('/team'):
            await message.channel.send('uoooooooo')


    # メッセージ受信時に動作する処理
    #@client.event
    #async def on_message(message):
        # メッセージ送信者がBotだった場合は無視する
        #if message.author.bot:
        #    return
        # 「/neko」と発言したら「にゃーん」が返る処理
        #print(message.content)
        #if message.content == f"/neko":


    # 返信する非同期関数を定義
    async def reply(message):
        reply = f'{message.author.mention} 呼んだ？' # 返信メッセージの作成
        await message.channel.send(reply) # 返信メッセージを送信

    # 発言時に実行されるイベントハンドラを定義
    @client.event
    async def on_message(message):
        print(len(message.content))

        if message.author.bot:
            return

        if client.user in message.mentions: # 話しかけられたかの判定
            await reply(message) # 返信する非同期関数を実行
            await message.channel.send('にゃーん')

        if message.content.startswith('/last_msg'):
            await message.channel.send('uoooooooo')



        #if message.content == "/neko":


    client.run(TOKEN)


def main():
    connect_discord()

main()