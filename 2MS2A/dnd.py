import json
from random import randint

import discord
from discord.ext import tasks, commands


def getData():
    with open("data.json", "r") as levelsFile:
        return json.loads(levelsFile.read())


def setData(_dict):
    with open("data.json", "w") as levelsFile:
        levelsFile.write(json.dumps(_dict))


levelxp = [0, 300, 900, 2700, 6500, 14000, 23000, 34000, 48000, 64000, 85000, 100000, 120000, 140000, 165000, 195000, 225000, 265000, 305000, 355000]


# noinspection PyCallingNonCallable
class DND(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ac = randint(1, 20)
        self.base = {
            "xp": 0,
            "level": 0,
            "health": 20,
            "class": "",
            "inventory": [],
            "stats": {
                "str": {"base": 0, "mod": 0},
                "dex": {"base": 0, "mod": 0},
                "con": {"base": 0, "mod": 0},
                "int": {"base": 0, "mod": 0},
                "wis": {"base": 0, "mod": 0},
                "cha": {"base": 0, "mod": 0}
            }
        }
        self.bonuses = {
            0: -5,
            2: -4,
            4: -3,
            6: -2,
            8: -1,
            10: 0,
            12: 1,
            14: 2,
            16: 3,
            18: 4,
            20: 5,
            22: 6,
            24: 7,
            26: 8,
            28: 9,
            30: 10
        }
        self.hell_ac.start()

    def cog_unload(self):
        self.hell_ac.cancel()

    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            try:
                data = getData()
                try:
                    level = data[message.author.name]["level"]
                    data[message.author.name]["xp"] += (randint(1, 10))
                except:
                    data[message.author.name] = self.base
                    level = data[message.author.name]["level"]
                    data[message.author.name]["xp"] += randint(1, 10)

                bonus = 2 if level < 5 else (3 if level < 9 else (4 if level < 13 else (5 if level < 17 else 6)))

                if message.channel.name == "hell":
                    roll = randint(1, 20) + bonus
                    if (roll < self.ac or roll - bonus == 1) and roll - bonus != 20:
                        await message.delete()
                        await message.channel.send("**%s** tried to send a message, but failed the roll!" % message.author.name)
                        if roll - bonus == 1:
                            await message.channel.send("**%s just nat 1'd!**" % message.author.name)
                    else:
                        await message.delete()
                        # await message.channel.send("(%s < %s+%s) **%s**: %s" % (self.ac, roll - bonus, bonus, message.author.name, message.content))
                        await message.channel.send("**%s**: %s" % (message.author.name, message.content))
                        if roll - bonus == 20:
                            await message.channel.send("**%s just nat 20'd!**" % message.author.name)
                        data[message.author.name]["xp"] += self.ac
                        if roll - bonus > 10:
                            data[message.author.name]["xp"] += randint(0, roll)

                else:
                    try:
                        words = data["banned words"]
                    except:
                        data["banned words"] = []
                        words = data["banned words"]

                    for word in words:
                        if word in message.content.lower() and not (message.content.startswith("2m.unban") or message.content.startswith("2m.ban")):
                            data[message.author.name]["health"] -= 1
                            await message.channel.send("Uh oh! You fucking idiot. You just said '%s'.\n\nDie." % word)
                            print("%s USED A BANNED WORD." % message.author.name)

                    if data[message.author.name]["xp"] >= levelxp[level]:
                        data[message.author.name]["level"] += 1
                        await message.channel.send("**%s** levelled up to level %s!" % (message.author.name, data[message.author.name]["level"]))
                        print("%s LEVELLED UP." % message.author.name)

                    if data[message.author.name]["health"] <= 0:
                        data[message.author.name] = self.base
                        await message.channel.send("Oop, **%s** is dead. Now you gotta reroll stats!" % message.author.name)
                        print("%s DIED." % message.author.name)
                setData(data)
            except:
                pass

    @tasks.loop(minutes=5)
    async def hell_ac(self):
        bots = discord.utils.get(self.bot.get_guild(677689511525875715).channels, name="bots")
        if randint(1, 100) <= 33:
            ac = randint(1, 20)
            self.ac = ac
            # await bots.send("__**Hell's AC is now %s!**__" % ac)
            print("HELL'S AC HAS BEEN REROLLED. (%s)" % self.ac)

    @commands.command(brief="Get the 10 highest levelled people in the server.")
    async def leaderboard(self, ctx):
        data = getData()
        scores = {"": 0}
        finals = {}
        for person in data:
            if person != "banned words":
                scores[person] = data[person]["xp"]
        for i in range(10):
            max = ""
            for j in scores:
                if scores[j] > scores[max]:
                    max = j
            finals[max] = scores[max]
            del scores[max]
        final = ["**%s** - %sxp" % (person, finals[person]) for person in finals]
        await ctx.send("\n".join(final))
        print("%s GOT THE XP LEADERBOARD." % ctx.author.name)

    @commands.command(brief="Roll up your stats.")
    async def rollstats(self, ctx, *, order):
        data = getData()
        try:
            if not (0 in (data[ctx.author.name]["stats"][key]["base"] for key in data[ctx.author.name]["stats"])):
                return await ctx.send("You've already rolled your stats! Theres no going back now.")
        except:
            data[ctx.author.name] = self.base
        order = order.split(" ")
        for item in order:
            if item not in ["str", "dex", "con", "int", "wis", "cha"]:
                return await ctx.send("Please use the correct stat names!\nThey are:\n%s" % ("\n".join(["str", "dex", "con", "int", "wis", "cha"])))
        final = []
        allrolls = []
        for i in range(6):
            allrolls.append([randint(1, 6) for x in range(4)])
        for arr in range(len(allrolls)):
            del allrolls[arr][allrolls[arr].index(min(allrolls[arr]))]
            allrolls[arr] = sum(allrolls[arr])
        allrolls.sort(reverse=True)
        for i in range(6):
            num = allrolls[i]
            tempnum = allrolls[i]
            if tempnum % 2 == 1:
                tempnum -= 1
            final.append("%s -> %s (%s)" % (order[i], num, self.bonuses[tempnum] if num < 10 else ("+%s" % self.bonuses[tempnum])))
            data[ctx.author.name]["stats"][order[i]] = {"base": num, "mod": self.bonuses[tempnum]}
        await ctx.send("\n".join(final))
        print("%s ROLLED THEIR STATS." % ctx.author.name)
        setData(data)

    # @commands.command(brief="Get the AC of hell.")
    # async def getac(self, ctx):
    #     await ctx.send("Hell's AC is currently **%s**!" % self.ac)
    #     print("%s GOT HELL'S CURRENT AC." % ctx.author.name)

    @commands.command(brief="Get information on a level.")
    async def levelinfo(self, ctx, level: int):
        if not level > 20:
            await ctx.send("__**Level %s Information**__\nNeeded XP: %s\nProficiency Bonus: %s" % (level, levelxp[level - 1], "+2" if level < 5 else ("+3" if level < 9 else ("+4" if level < 13 else ("+5" if level < 17 else "+6")))))
        else:
            await ctx.send("That level is too high! Level 20 is the maximum.")
        print("%s GOT LEVEL INFORMATION. (%s)" % (ctx.author.name, level))

    @commands.command(brief="Get your current level and XP.")
    async def stats(self, ctx):
        data = getData()
        level = data[ctx.author.name]["level"]
        bonus = 2 if level < 5 else (3 if level < 9 else (4 if level < 13 else (5 if level < 17 else 6)))
        await ctx.send(
            "__**%s's Information**__\nHealth: %s\nLevel: %s\nXP: %s\nProficiency Bonus: +%s\n\n%s" % (ctx.author.name, data[ctx.author.name]["health"], data[ctx.author.name]["level"], data[ctx.author.name]["xp"], bonus, "\n".join(
                ["%s: %s (%s)" % (key, data[ctx.author.name]["stats"][key]["base"], data[ctx.author.name]["stats"][key]["mod"]) for key in data[ctx.author.name]["stats"]])))
        print("%s GOT THEIR LEVEL INFORMATION." % ctx.author.name)


def setup(bot):
    bot.add_cog(DND(bot))
