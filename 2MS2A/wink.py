from random import choice

import discord
import yippi as yip
from discord.ext import commands


class wink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief=";) (but bullying people)")
    async def yiff(self, ctx, person, rating, *, tags=""):
        server = ctx.guild
        tags = tags.split(" ")
        if person != "random":
            user = discord.utils.get(server.members, name=person)
        else:
            user = choice(server.members)
        results = yip.search.post(tags, rating=rating, limit=10000)
        try:
            post = choice(results)
            post.download("img/SPOILER_esix2.png")
            if user.dm_channel:
                await user.dm_channel.send(file=discord.File("img/SPOILER_esix2.png"))
            else:
                await user.create_dm()
                await user.dm_channel.send(file=discord.File("img/SPOILER_esix2.png"))
            await ctx.send("**%s** yiffed **%s**!" % (ctx.author.name, user.name))
        except IndexError:
            await ctx.send("There weren't any posts with those tags!")
        print("%s JUST YIFFED %s. (%s)" % (ctx.author.name, user.name, rating))

    @commands.command(brief=";)")
    async def gimme(self, ctx, *, tags=""):
        tags = tags.split(" ")
        if ctx.channel.is_nsfw():
            results = yip.search.post(tags, rating="e", limit=10000)
            post = choice(results)
            post.download("img/SPOILER_esix.png")
            await ctx.send(file=discord.File("img/SPOILER_esix.png"))
        else:
            results = yip.search.post(tags, rating="s", limit=10000)
            post = choice(results)
            post.download("img/SPOILER_esix.png")
            await ctx.send(file=discord.File("img/SPOILER_esix.png"))
        print("%s GOT A%s IMAGE FROM ESIX." % (ctx.author.name, "N EXPLICIT" if ctx.channel.is_nsfw() else " SAFE"))


def setup(bot):
    bot.add_cog(wink(bot))
