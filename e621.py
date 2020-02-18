import os
import sys
from random import *

from discord.ext import commands
from yippi import *


def clear(): return os.system("cls")


sys.path.append("T:/all")
bot = commands.Bot(command_prefix="hey, ")


@bot.command()
async def give(ctx, *, args=""):
    args = args.split(" ")

    args = args[1:]

    if args[0] in ["a", "an"]:
        args[0] = 1

    rating = args[1]
    rating = rating[0]

    if not rating in ["s", "q", "e"]:
        rating = False

    tags = []
    try:
        tags = args[args.index("tags") + 1:]
    except:
        try:
            tags = args[args.index("tag") + 1:]
        except:
            tags = []

    final = []
    if rating:
        results = search.post(tags, rating=rating, limit=1000000)
    else:
        results = search.post(tags, limit=1000000)

    for i in range(int(args[0])):
        post = choice(results)
        final.append(post.file_url)

    await ctx.send("\n".join(final))


with open("T:/all/e621.txt", "r") as token:
    bot.run(token.read())
