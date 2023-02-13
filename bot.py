import discord
import asyncio
import json

time_zones = ["UTC", "ECT", "EET", "ART", "EAT", "IST", "MIT", "HST", "AST", "PST", "PNT", "MST", "CST", "EST", "IET", "PRT", "CNT", "AGT", "BET"]

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    while True:
        role_count = {}
        for guild in client.guilds:
            for role in guild.roles:
                if role.name in time_zones:
                    role_count[role.name] = len(role.members)
        
        timezones = {
            "UTC": "Universal Coordinated Time > GMT-0:00",
            "ECT": "European Central Time > GMT+1:00",
            "EET": "Eastern European Time > GMT+2:00",
            "ART": "(Arabic) Egypt Standard Time > GMT+2:00",
            "EAT": "Eastern African Time > GMT+3:00",
            "IST": "India Standard Time > GMT+5:30",
            "MIT": "Midway Islands Time > GMT-11:00",
            "HST": "Hawaii Standard Time > GMT-10:00",
            "AST": "Alaska Standard Time > GMT-9:00",
            "PST": "Pacific Standard Time > GMT-8:00",
            "PNT": "Phoenix Standard Time > GMT-7:00",
            "MST": "Mountain Standard Time > GMT-7:00",
            "CST": "Central Standard Time > GMT-6:00",
            "EST": "Eastern Standard Time > GMT-5:00",
            "IET": "Indiana Eastern Standard Time > GMT-5:00",
            "PRT": "Puerto Rico and US Virgin Islands Time > GMT-4:00",
            "CNT": "Canada Newfoundland Time > GMT-3:30",
            "AGT": "Argentina Standard Time > GMT-3:00",
            "BET": "Brazil Eastern Time > GMT-3:00",
        }

        timezone_descriptions = ""
        for timezone, description in timezones.items():
            timezone_count = role_count[timezone]
            timezone_descriptions += f"({timezone_count}) {timezone} > {description}\n"

        content = discord.Embed(title="Timezones", description=timezone_descriptions, color=0x00ff00)

        
        update = False

        channel = client.get_channel(replace_me)
        messages = [message async for message in channel.history(limit=5)]
        for message in messages:
            if message.embeds:
                for emb in message.embeds:
                    if emb.title == "Timezones":
                        update = True
                        await message.edit(embed=content)
                        break

        if not update:
            await channel.send(embed=content)

        await asyncio.sleep(10)

client.run('replace_me')