import asyncio as a
import os
import sys
from random import *

import gspread
from discord.ext import commands
from oauth2client.service_account import ServiceAccountCredentials


def clear(): return os.system("cls")


sys.path.append("T:/all")
bot = commands.Bot(command_prefix="g.")

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name("T:/all/WHWGcreds.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Who Has What Game").sheet1

sheet_dict = {
    "games": sheet.col_values(1)[1:],
    "prices": sheet.col_values(2)[1:],
    "genres": sheet.col_values(3)[1:],
    "toaster": sheet.col_values(sheet.find("toaster").col)[1:],
    "toaster_ratings": sheet.col_values(sheet.find("toaster").col + 1)[1:],
    "nate": sheet.col_values(sheet.find("nate").col)[1:],
    "nate_ratings": sheet.col_values(sheet.find("nate").col + 1)[1:],
    "jonathan": sheet.col_values(sheet.find("jonathan").col)[1:],
    "jonathan_ratings": sheet.col_values(sheet.find("jonathan").col + 1)[1:],
    "kellen": sheet.col_values(sheet.find("kellen").col)[1:],
    "kellen_ratings": sheet.col_values(sheet.find("kellen").col + 1)[1:],
    "satchel": sheet.col_values(sheet.find("satchel").col)[1:],
    "satchel_ratings": sheet.col_values(sheet.find("satchel").col + 1)[1:],
    "quinn": sheet.col_values(sheet.find("quinn").col)[1:],
    "quinn_ratings": sheet.col_values(sheet.find("quinn").col + 1)[1:],
    "connor": sheet.col_values(sheet.find("connor").col)[1:],
    "connor_ratings": sheet.col_values(sheet.find("connor").col + 1)[1:],
}


@bot.event
async def on_ready():
    clear()
    print("\n\nrunning\n\n")


@bot.command()
async def wait(ctx):
    await a.sleep(105)
    await ctx.send("Times up!")


@bot.command(brief="(What do they own) - Get a list of all games someone has")
async def wdto(ctx, *, args=""):
    args = args.split(", ")
    col = sheet_dict[args[0]]
    ratings = sheet_dict[args[0] + "_ratings"]
    games = sheet_dict["games"]
    arr1 = []
    for i in range(len(col)):
        if col[i] in ["I", "NI", "CP"]:
            if len(args) == 1 or args[1] == "r":
                arr1.append("(" + str(ratings[i]) + ") **" + str(games[i]) + "**")
            else:
                arr1.append(games[i])
    arr1.sort()
    print("%s | %s | GOT ALL GAMES %s OWNS" % (ctx.guild.name.upper(), ctx.author.name.upper(), args[0].upper()))
    await ctx.send("\n".join(arr1))


@bot.command(brief="(What do they share) - Get a list of all games two people share")
async def wdts(ctx, *, args=""):
    args = args.split(", ")
    games = sheet_dict["games"]
    dict = {}
    for game in games:
        dict[game] = [0, []]
    arr = []
    arglen = len(args)
    nr = False
    if args[-1] == "nr":
        arglen = len(args) - 1
        nr = True
    for num in range(arglen):
        col = sheet_dict[args[num]]
        ratings = sheet_dict[args[num] + "_ratings"]
        for i in range(len(col)):
            if col[i] in ["I", "NI", "CP"]:
                if nr:
                    dict[games[i]][0] = dict[games[i]][0] + 1
                else:
                    if ratings[i] != "N/A":
                        dict[games[i]][0] = dict[games[i]][0] + 1
                        dict[games[i]][1].append(float(ratings[i]))
    for game in dict:
        if dict[game][0] == (arglen):
            if nr:
                arr.append(game)
            else:
                arr.append("(%s) **%s**" % (round((sum(dict[game][1]) / len(dict[game][1]) * 10)) / 10, game))
    arr.sort()
    print("%s | %s | GOT ALL GAMES %s SHARE" % (ctx.guild.name.upper(), ctx.author.name.upper(), args))
    await ctx.send("\n".join(arr))


@bot.command(brief="(Get game that they own) - Get a random game someone owns")
async def ggtto(ctx, *, args=""):
    args = args.split(", ")
    col = sheet_dict[args[0]]
    ratings = sheet_dict[args[0] + "_ratings"]
    games = sheet_dict["games"]
    arr1 = []
    for i in range(len(col)):
        if col[i] in ["I", "NI", "CP"]:
            if len(args) == 1 or args[1] == "r":
                try:
                    for x in range(int(ratings[i]) * 100):
                        arr1.append("(%s) **%s**" % (ratings[i], games[i]))
                except:
                    pass
            else:
                arr1.append(games[i])
    print("%s | %s | GOT A RANDOM GAME %s OWNS" % (ctx.guild.name.upper(), ctx.author.name.upper(), args[0].upper()))
    await ctx.send(choice(arr1))


@bot.command(brief="(Get game that they share) - Get a random game from a list of games that people share")
async def ggtts(ctx, *, args=""):
    args = args.split(", ")
    games = sheet_dict["games"]
    dict = {}
    for game in games:
        dict[game] = [0, []]
    arr = []
    arglen = len(args)
    nr = False
    if args[-1] == "nr":
        arglen = len(args) - 1
        nr = True
    for num in range(arglen):
        col = sheet_dict[args[num]]
        ratings = sheet_dict[args[num] + "_ratings"]
        for i in range(len(col)):
            if col[i] in ["I", "NI", "CP"]:
                if nr:
                    dict[games[i]][0] = dict[games[i]][0] + 1
                else:
                    if ratings[i] != "N/A":
                        dict[games[i]][0] = dict[games[i]][0] + 1
                        dict[games[i]][1].append(float(ratings[i]))
    for game in dict:
        if dict[game][0] == (arglen):
            if nr:
                arr.append(game)
            else:
                for i in range(round((sum(dict[game][1]) / len(dict[game][1])))):
                    arr.append("(%s) **%s**" % (round((sum(dict[game][1]) / len(dict[game][1]) * 10)) / 10, game))
    print("%s | %s | GOT A RANDOM GAME %s SHARE" % (ctx.guild.name.upper(), ctx.author.name.upper(), args))
    await ctx.send(choice(arr))


@bot.command(brief="(Get games) - Get a list of all the games on the sheet")
async def gg(ctx):
    games = sheet_dict["games"]
    prices = sheet_dict["prices"]
    arr = []
    for i in range(len(games)):
        arr.append("(%s) **%s**" % (prices[i], games[i]))
    arr.sort()
    print("%s | %s | GOT ALL GAMES ON THE SHEET" % (ctx.guild.name.upper(), ctx.author.name.upper()))
    await ctx.send("\n".join(arr))


@bot.command(brief="(Refresh sheet) - Refresh the data the bot has stored")
async def rs(ctx):
    try:
        sheet_dict = {
            "games": sheet.col_values(1)[1:],
            "prices": sheet.col_values(2)[1:],
            "genres": sheet.col_values(3)[1:],
            "toaster": sheet.col_values(sheet.find("toaster").col)[1:],
            "toaster_ratings": sheet.col_values(sheet.find("toaster").col + 1)[1:],
            "nate": sheet.col_values(sheet.find("nate").col)[1:],
            "nate_ratings": sheet.col_values(sheet.find("nate").col + 1)[1:],
            "jonathan": sheet.col_values(sheet.find("jonathan").col)[1:],
            "jonathan_ratings": sheet.col_values(sheet.find("jonathan").col + 1)[1:],
            "kellen": sheet.col_values(sheet.find("kellen").col)[1:],
            "kellen_ratings": sheet.col_values(sheet.find("kellen").col + 1)[1:],
            "satchel": sheet.col_values(sheet.find("satchel").col)[1:],
            "satchel_ratings": sheet.col_values(sheet.find("satchel").col + 1)[1:],
            "quinn": sheet.col_values(sheet.find("quinn").col)[1:],
            "quinn_ratings": sheet.col_values(sheet.find("quinn").col + 1)[1:],
            "connor": sheet.col_values(sheet.find("connor").col)[1:],
            "connor_ratings": sheet.col_values(sheet.find("connor").col + 1)[1:],
        }
        await ctx.send("Refreshed!")
    except:
        await ctx.send("Try again in a minute, I ran out of read requests. (or my oauth expired)")
    print("%s | %s | REFRESHED THE BOTS DATA (OR TRIED TO)" % (ctx.guild.name.upper(), ctx.author.name.upper()))


with open("T:/all/whwgcreds.txt", "r") as token:
    bot.run(token.read())
