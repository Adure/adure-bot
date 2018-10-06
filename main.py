from auth import bot_token
import logging
import strawpoll as spoll
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='/')

logger = logging.getLogger('main')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('logs.log')
fh.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s: %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)


@bot.command()
async def strawpoll(ctx, question, *args):
    api = spoll.API()
    options = []
    for i in args:
        options.append(i)

    topoll = spoll.Poll(question, options, multi=False)
    return_poll = await api.submit_poll(poll=topoll)
    await ctx.send(return_poll.url)

@bot.command()
async def helplines(ctx):
    await ctx.send("""**United States** - <https://www.nami.org/find-support/nami-helpline/top-25-helpline-resources>
**Canada** - <https://suicideprevention.ca/need-help/>
**United Kingdom** - <http://www.supportline.org.uk/problems/suicide.php>

**Australia** - For help ASAP Australia-Wide:

Lifeline: 13 11 14
Kids Helpline: 1800 55 1800
Suicide Call Back Service: 1300 659 467

<https://bluepages.anu.edu.au/index.php?id=australian-crisis-numbers>

**Other useful links:**

Beyond Blue: 1300 22 4636 / <https://www.beyondblue.org.au/>
Black Dog Institute: <https://www.blackdoginstitute.org.au/>
Headspace: <https://www.headspace.org.au/>

**New Zealand** - <https://www.mentalhealth.org.nz/get-help/in-crisis/helplines/>

**List of suicide crisis lines if you are international or travelling:**

<https://en.wikipedia.org/wiki/List_of_suicide_crisis_lines>""")


@bot.command()
async def poll(ctx, *, arg):
    await ctx.message.delete()
    embed = discord.Embed(title=ctx.author.name+"#"+str(ctx.author.discriminator), description=arg, color=0x006400)
    message = await ctx.send(embed=embed)
    good = bot.get_emoji(498003199102418944)
    bad = bot.get_emoji(498003199257477120)
    await message.add_reaction(good)
    await message.add_reaction(bad)

@bot.event
async def on_ready():
    logger.info(f"Logged in as {bot.user.name} - {bot.user.id}")

bot.run(bot_token)