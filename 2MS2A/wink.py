from random import choice

import discord
import yippi as yip
from discord.ext import commands


class wink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief=";) (but bullying people)")
    async def yiff(self, ctx, person: discord.Member, rating, message="", *, tags=""):
        tags = tags.split(" ")
        results = yip.search.post(tags, rating=rating, limit=10000)
        try:
            post = choice(results)
            post.download("img/%sesix2.png" % ("SPOILER_" if rating in ["e", "q"] else ""))
            if person.dm_channel:
                await person.dm_channel.send(message, file=discord.File(
                    "img/%sesix2.png" % ("SPOILER_" if rating in ["e", "q"] else "")))
            else:
                await person.create_dm()
                await person.dm_channel.send(message, file=discord.File(
                    "img/%sesix2.png" % ("SPOILER_" if rating in ["e", "q"] else "")))
            if person.name == ctx.author.name:
                await ctx.send("**%s** yiffed themself!" % ctx.author.name)
            else:
                await ctx.send("**%s** yiffed **%s**!" % (ctx.author.name, person.name))
        except IndexError:
            await ctx.send("There weren't any posts with those tags!")
        except:
            await ctx.send("Something went wrong! Maybe the file was too big?")
        print("%s JUST YIFFED %s. (%s)" % (ctx.author.name, person.name, rating))

    @commands.command(brief=";)")
    async def gimme(self, ctx, amount: int = 1, rating="s", *, tags=""):
        tags = tags.split(" ")
        if amount > 5:
            return await ctx.send("You can only get 5 images maximum!")
        results = yip.search.post(tags, rating=rating, limit=10000)
        try:
            for i in range(amount):
                post = choice(results)
                post.download("img/%sesix%s.png" % ("SPOILER_" if rating in ["e", "q"] else "", i))
            images = [discord.File("img/%sesix%s.png" % ("SPOILER_" if rating in ["e", "q"] else "", i)) for i in range(amount)]
            await ctx.send(files=images)
        except IndexError:
            await ctx.send("Those tags have no results!")
        except:
            await ctx.send("Something went wrong! Maybe the file was too big?")
        print("%s GOT AN IMAGE FROM ESIX." % ctx.author.name)


def setup(bot):
    bot.add_cog(wink(bot))
