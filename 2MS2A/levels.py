import json
from random import randint

from discord.ext import commands


def getLevels():
    with open("levels.json", "r") as levelsFile:
        return json.loads(levelsFile.read())


def setLevels(dict):
    with open("levels.json", "w") as levelsFile:
        levelsFile.write(json.dumps(dict))


levelxp = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000]


class Levels(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            levels = getLevels()
            try:
                levels[message.author.name]["xp"] += (randint(1, 10))
            except KeyError:
                levels[message.author.name] = {"xp": randint(1, 10), "level": 0}

            if levels[message.author.name]["xp"] >= levelxp[levels[message.author.name]["level"]]:
                levels[message.author.name]["level"] += 1
                await message.channel.send("**%s** levelled up to level %s!" % (message.author.name, levels[message.author.name]["level"]))

            setLevels(levels)

    @commands.command(brief="Get information on a level.")
    async def levelinfo(self, ctx, level: int):
        if not level > 20:
            await ctx.send("__**Level %s Information**__\nNeeded XP: %s" % (level, levelxp[level - 1]))
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
