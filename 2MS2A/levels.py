import json
from random import randint

import discord
from discord.ext import tasks, commands


def getLevels():
    with open("levels.json", "r") as levelsFile:
        return json.loads(levelsFile.read())


def setLevels(_dict):
    with open("levels.json", "w") as levelsFile:
        levelsFile.write(json.dumps(_dict))


levelxp = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000]


class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ac = randint(1, 20)
        self.hell_ac.start()

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            levels = getLevels()
            level = levels[message.author.name]["level"]
            bonus = 2 if level < 5 else (3 if level < 9 else (4 if level < 13 else (5 if level < 17 else 6)))
            try:
                levels[message.author.name]["xp"] += (randint(1, 10))
            except KeyError:
                levels[message.author.name] = {"xp": randint(1, 10), "level": 0}

            if message.channel.name == "hell":
                roll = randint(1, 20) + bonus
                if roll <= self.ac:
                    await message.delete()
                    await message.channel.send("(%s > %s+%s) **%s** tried to send a message, but failed the roll!" % (self.ac, roll - bonus, bonus, message.author.name))
                else:
                    await message.delete()
                    await message.channel.send("(%s < %s+%s) **%s**: %s" % (self.ac, roll - bonus, bonus, message.author.name, message.content))

            elif levels[message.author.name]["xp"] >= levelxp[level]:
                levels[message.author.name]["level"] += 1
                await message.channel.send("**%s** levelled up to level %s!" % (message.author.name, levels[message.author.name]["level"]))

            setLevels(levels)

    @tasks.loop(minutes=5)
    async def hell_ac(self):
        hell = discord.utils.get(self.bot.get_guild(677689511525875715).channels, name="hell")
        if randint(1, 100) <= 33:
            ac = randint(1, 20)
            self.ac = ac
            await hell.send("__**Hell's AC is now %s!**__" % ac)

    @commands.command(brief="Reroll the AC of hell.")
    async def rerollac(self, ctx):
        if ctx.author.name != "Toaster":
            await ctx.send("Only Toaster can do that!")
        else:
            self.ac = randint(1, 20)
            await ctx.send("Hell's AC is now %s!" % self.ac)

    @commands.command(brief="Get the AC of hell.")
    async def getac(self, ctx):
        await ctx.send("Hell's AC is currently **%s**!" % self.ac)

    @commands.command(brief="Get information on a level.")
    async def levelinfo(self, ctx, level: int):
        if not level > 20:
            await ctx.send("__**Level %s Information**__\nNeeded XP: %s\nProficiency Bonus: %s" % (level, levelxp[level - 1], "+2" if level < 5 else ("+3" if level < 9 else ("+4" if level < 13 else ("+5" if level < 17 else "+6")))))
        else:
            await ctx.send("That level is too high! Level 20 is the maximum.")
        print("%s GOT LEVEL INFORMATION. (%s)" % (ctx.author.name, level))

    @commands.command(brief="Get your current level and XP.")
    async def level(self, ctx):
        levels = getLevels()
        await ctx.send("__**%s's Information**__\nLevel: %s\nXP: %s" % (ctx.author.name, levels[ctx.author.name]["level"], levels[ctx.author.name]["xp"]))
        print("%s GOT THEIR LEVEL INFORMATION." % ctx.author.name)


def setup(bot):
    bot.add_cog(Levels(bot))
