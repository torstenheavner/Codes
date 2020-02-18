import json

from discord.ext import commands


def getIdeas():
    with open("ideas.json", "r") as ideasFile:
        return json.loads(ideasFile.read())


def setIdeas(input):
    with open("ideas.json", "w") as ideasFile:
        ideasFile.write(json.dumps(input))


class Ideas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief="List all ideas, or get info from one specific idea.", usage="<idea>")
    async def ideas(self, ctx, idea=""):
        ideas = getIdeas()
        if idea == "":
            out = []
            if ideas == {}:
                await ctx.send("There are no ideas yet!")
            else:
                for item in ideas:
                    out.append("**%s** - %s (%s)" % (item, ideas[item]["brief"], ideas[item]["author"]))

                await ctx.send("\n".join(out))
        else:
            if ideas[idea]:
                await ctx.send(
                    "**%s** - %s (%s)\n%s" % (idea, ideas[idea]["brief"], ideas[idea]["author"], ideas[idea]["desc"]))
            else:
                await ctx.send("That idea doesn't exist!")
        print("%s LISTED ALL IDEAS." % ctx.author.name)

    @commands.command(brief="Add a new idea.", usage="[name] [brief] [description]")
    async def idea(self, ctx, name="n/a", brief="n/a", desc="n/a"):
        ideas = getIdeas()

        if name in ["n/a", ""]:
            await ctx.send("You must input a name!")
        elif brief in ["n/a", ""]:
            await ctx.send("You must input a brief!")
        elif desc in ["n/a", ""]:
            await ctx.send("You must input a description!")
        else:
            ideas[name] = {"brief": brief, "desc": desc, "author": ctx.message.author.name}
            await ctx.send("Idea added!\n**%s** - %s" % (name, brief))

        setIdeas(ideas)
        print("%s ADDED A NEW IDEA. %s" % (ctx.author.name, name))

    @commands.command(brief="Change information about an idea.",
                      usage="[name] [name/brief/desc] [what to change it to]")
    async def changeidea(self, ctx, name="n/a", which="n/a", new="n/a"):
        ideas = getIdeas()

        if name in ["n/a", ""]:
            await ctx.send("You must input the name of the idea to change!")
        elif which.lower() not in ["name", "brief", "desc"]:
            await ctx.send("You must input which to change!")
        elif new in ["n/a", ""]:
            await ctx.send("You must input what to change it to!")
        else:
            if which == "name":
                ideas[new] = ideas[name]
                del ideas[name]
                await ctx.send("Idea changed!\n**%s** - %s" % (new, ideas[new]["brief"]))
            else:
                ideas[name][which.lower()] = new
                await ctx.send("Idea changed!\n**%s** - %s" % (name, ideas[name]["brief"]))

        setIdeas(ideas)
        print("%s CHANGED AN IDAE. %s" % (ctx.author.name, name))

    @commands.command(brief="Forget an idea.", usage="[name]")
    async def forget(self, ctx, name="n/a"):
        ideas = getIdeas()

        if name in ["n/a", ""]:
            await ctx.send("You must input a name!")
        else:
            del ideas[name]
            await ctx.send("Idea removed!")

        setIdeas(ideas)
        print("%s REMOVED AN IDEA. %s" % (ctx.author.name, name))


def setup(bot):
    bot.add_cog(Ideas(bot))
