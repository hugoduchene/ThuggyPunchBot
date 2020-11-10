import discord
from random import randint


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.content.startswith('!punch'):
            channel = message.channel
            channel = message.author.voice

            await message.channel.send("Actuellement entrain de te boyave dans le vocale !")
            vc = await channel.channel.connect()
            vc = self.voice_clients[-1]
            source = "./assets/mp3/" + str(randint(0, 2))
            vc.play(discord.FFmpegPCMAudio(
                executable="C:/ffmpeg/bin/ffmpeg.exe", source=source + '.mp3'
                )
            )

            while vc.is_playing():
                continue
            await vc.disconnect()


def launch_bot(TOKEN):
    client = MyClient()
    client.run(TOKEN)
