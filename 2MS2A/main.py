import os
import os
import sys

# from cv2 import *
from discord.ext import commands


# try:
#     cam = VideoCapture(0)
# except:
#     cam = None


def clear(): return os.system("cls")


sys.path.append("T:/all")
bot = commands.Bot(command_prefix="2m.")

with open("cogs.txt", "r") as file:
    cogs = file.read()
for extension in cogs.split("\n"):
    bot.load_extension(extension)
    print("%s LOADED." % extension)


@bot.event
async def on_ready():
    clear()
    print("\nTOO MUCH STUFF TO AUTOMATE\nONLINE\n\n")


@bot.command(brief="Play ping pong.")
async def ping(ctx):
    await ctx.send("Pong!")
    print("%s PINGED THE BOT." % ctx.author.name)


# @bot.command(brief="Take a picture using Toaster's webcam.")
# async def snapshot(ctx):
#     global cam
#     if not cam:
#         s, img = cam.read()
#         imwrite("img/webcam.jpg", img)
#         await ctx.send(file=discord.File("img/webcam.jpg"))
#         print("%s INVADED TOASTER'S PRIVACY" % ctx.author.name)
#     else:
#         await ctx.send("Toaster's camera is off!")


@bot.command(name="reload", brief="Reload all of the bots cogs.")
async def _reload(ctx, cog="all"):
    log = []
    with open("cogs.txt", "r") as file:
        cogs = file.read()
    if cog == "all":
        for extension in cogs.split("\n"):
            try:
                bot.unload_extension(extension)
                bot.load_extension(extension)
                log.append("**%s** reloaded successfully." % extension)
            except:
                bot.load_extension(extension)
                log.append("**%s** loaded successfully." % extension)

        await ctx.send("\n".join(log))
        print("%s RELOADED THE BOTS MODULES." % ctx.author.name)
    else:
        try:
            bot.unload_extension(cog)
            bot.load_extension(cog)
            await ctx.send("**%s** reloaded successfully." % cog)
        except:
            bot.load_extension(cog)
            await ctx.send("**%s** loaded successfully." % cog)
        print("%s RELOADED THE %s MODULE." % (ctx.author.name, cog))


with open("T:/all/2ms2a_creds.txt", "r") as token:
    bot.run(token.read())
