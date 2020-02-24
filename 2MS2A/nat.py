import json
import random

import discord
import numpy as np
from discord.ext import commands


class nat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.people=[]
        
    @commands.Cog.listener()
    async def on_message(self, message):
        if not message.author.bot:
            if message.author.name in self.people:
                message.channel.send (random.choice(["no.", "wrong.", "incorrect.", "i dont think so.", "nope.", "nope, i dont want that.", "thats no good.", "invalid.", "i dont like it."]))

    @commands.command(brief="disagrees with a user")
    async def disagree(self, ctx, person:discord.Member):
        self.people.append(person.name)
        await ctx.send(person.name + " is now invalid") 
   
   
   
   
   
   
   
   
def setup(bot):
    bot.add_cog(nat(bot))
