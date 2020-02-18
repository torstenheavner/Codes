from random import choice

import discord
import yippi as yip
from discord.ext import commands


class wink(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief=";)")
    async def gimme(self, ctx, *, args=""):
        tags = args.split(" ")
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
