import random

from discord.ext import commands


### CHANGE "example" IN THE NEXT LINE TO WHATEVER YOU WANT YOUR CATEGORY TO BE CALLED ###
### YOU MUST ALSO CHANGE IT AT THE END OF THE FILE ###
### THEN, ADD THE NAME OF THE FILE TO cogs.txt ###
class example(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="this is a command description")
    async def command_name(self, ctx):
        # ctx is short for context
        # it includes the channel, server, author, etc.

        author = ctx.author
        author_name = ctx.author.name

        server = ctx.guild
        server_name = ctx.guild.name

        # to send a message in the same channel the command was sent in...
        await ctx.send("put your message here")

        # generating a random number
        # for this, you have to put "import random" at the top of the file
        number = random.randint(0, 10)

        # picking randomly from an array (good for randomly choosing strings)
        # for this, you need to import random as well
        string = random.choice(["put", "array", "of", "whatever", "here"])

    @commands.command(brief="this is another command")
    async def second_command(self, ctx, argument1, argument2="bruh"):
        # this is how you use arguments.
        # arguments are always separated by space, but can be more than one word if surrounded in quotes
        # to have an argument have a default, do something like argument2
        await ctx.send(argument1, argument2)  # send a message of the arguments

        # to format a string with variables
        await ctx.send("argument 1: %s" % argument1)
        # or with multiple variables
        await ctx.send("argument 1: %s\nargument 2: %s" % (argument1, argument2))  # \n is a linebreak


def setup(bot):
    bot.add_cog(example(bot))
