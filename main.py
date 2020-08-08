#!/usr/bin/python3
import time
import os
import math
import random
import discord
from discord.ext import commands

###################

badjokes = []

with open("badjokes") as jokefile:
    badjokes = jokefile.read().split("\n-----\n")

print(badjokes)

raremessage = "WENN DU DAS LIEST BIST DU DER GEWINNER VON GAR NICHTS! ABER DIESE MELDUNG IST WIRKLICH SELTEN ALSO FREU DICH VERDAMMT NOCH MAL! (Die Chance, dass du deine Zeit verschwendest ist übrigens hoch.)"

helpmessage = "-------------------------OBB-HELP----------------------\n"
helpmessage += "Syntax: obb![command] egal ob mit oder ohne Leerzeichen\n"
helpmessage += "-------------------------------------------------------\n"
helpmessage += "ping - Testcommand um zu sehen ob der Bot online ist\n"
helpmessage += "countto - Testcommand der zur angegebenen Zahl zählt. (Bsp. obb!countto 10)\n"
helpmessage += "whoami - Testcommand, der den Namen des Nachrichtenauthors zurückgibt.\n"
helpmessage += "wait - Testcommand, der eine angegebene Zeit in Sekunden wartet. (Bsp. obb!wait 5 -> Timer für 5 Sekunden)\n"
helpmessage += "coinflip - Gibt entweder \"Kopf\" oder \"Zahl\" zurück.\nrolladie / würfel - Gibt eine zufällige Zahl von 1 bis 6 zurück.\n"
helpmessage += "joke / witz - Antwortet mit einem unglaublich schlechten Witz\n"
helpmessage += "help - Gibt diese Hilfemeldung zurück\n"
helpmessage += "allhelp - Gibt eine PDF-Hilfe-Datei zurück in der alle wichtigen Commands aller Bots auf JWars aufgelistet sind.\n"

#####################

TOKEN = "GET YOUR OWN TOKEN DUDE"
PREFIX = "obb!"

class BotClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
        await self.change_presence(activity=discord.Game(name="obb!help", type=3))

    async def on_message(self, message):
        if message.author == self.user:
            return
        if PREFIX == message.content[:len(PREFIX)].lower():
            command = message.content.lower().split(PREFIX, 2)[1].strip()
            print(f"[{message.author.name}] {command}")

            if "ping" in command:
                await message.channel.send("pong")
            if "countto" in command:
                countto = int(message.content.split("countto", 2)[1].strip(), 10)
                for i in range(countto):
                    time.sleep(0.2)
                    await message.channel.send(str(i+1))
            if "whoami" in command:
                await message.channel.send(message.author.name)
            if "wait" in command:
                waittime = int(message.content.split("wait", 2)[1].strip(), 10)
                await message.channel.send(f"@{message.author.name} setting timer for {waittime} seconds...")
                time.sleep(waittime)
                await message.channel.send(f"@{message.author.name} time's run out!")
            if command == "coinflip":
                num = random.randint(0,10)
                if num > 5:
                    await message.channel.send(f"@{message.author.name} Kopf ({num})")
                else:
                    await message.channel.send(f"@{message.author.name} Zahl ({num})")
            if command == "rolladie" or command == "würfel":
                num = (ord(os.urandom(1)) / 255) * 6 + 1
                num = math.floor(num)
                await message.channel.send(f"@{message.author.name} {str(num)}")
            if command == "joke" or command == "witz":
                if random.randint(0,5000) == 2500:
                    await message.channel.send(raremessage)
                    return
                else:
                    await message.channel.send(badjokes[random.randint(0,len(badjokes)-1)])
            if command == "help":
                await message.channel.send(helpmessage)
            if command == "allhelp":
                await message.channel.send(file=discord.File("/home/moritz/ohboybot1/Help.pdf"))
            if command == "bottest":
                await message.channel.send("r!play Kalinka")
client = BotClient()
client.run(TOKEN)

