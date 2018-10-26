import discord
from discord.ext import commands
import datetime
import time
import random
from random import randint
import aiohttp
import json
import sys
import traceback
import os

bot = commands.Bot(command_prefix='a!')

@bot.event
async def on_ready():
    print("logged in")
    await bot.change_presence(activity=discord.Game(name="a!"))


@bot.command(pass_context=True)
async def userinfo(ctx, user: discord.Member):
    """

    UserInfo (Forces The Bot To Get Data Of Someone) object
    """
    embed = discord.Embed(color=0x8B0000)
    embed.add_field(name="NAME OF THE ACCOUNT IS:", value="{}".format(user.name), inline=True)
    embed.add_field(name="NAME IS:", value="{}".format(user.display_name), inline=True)
    embed.add_field(name="ID IS:", value="{}".format(user.id), inline=False)
    embed.add_field(name="CREATED  AT:", value="{}".format(user.created_at), inline=False)
    embed.add_field(name="JOINED AT:", value="{}".format(user.joined_at), inline=False)
    embed.add_field(name="STATUS IS:", value="{}".format(user.status), inline=False)
    embed.set_thumbnail(url=user.avatar_url)
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def ping(ctx):
    """

    Ping (Forces The Bot To Tell Your Ping) object
    """
    channel = ctx.message.channel
    t1 = time.perf_counter()
    t2 = time.perf_counter()
    embed = discord.Embed(title=None, description='Ping: {} ms'.format(round((t2 - t1) * 1000)), color=0x8B0000)
    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    """

    Kick (Only Users That Have Permissions.kick_members) object
    """
    if ctx.author.guild_permissions.kick_members:
        embed = discord.Embed(color=0x8B0000)
        embed.add_field(name="GOT KICKED BY:", value=ctx.message.author.name)
        embed.add_field(name="USER NAME IS:", value=user.name)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="USER ID IS:", value=user.id)
        await ctx.send(embed=embed)
        await ctx.guild.kick(user)
    else:
        embed = discord.Embed(title=":bangbang: ERROR!", description="NO PERMISSIONS!", color=0x8B0000)
        await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def roast(ctx, member: discord.Member):
    """

    Roast (Forces The Bot To Roast A User) object
    """
    await ctx.send(member.mention)
    await ctx.send(random.choice(
        ['**How mentally retarded are you?**', 'I’d give you a nasty look but you’ve already got one.**',
         '**Gay? I’m straighter than the pole your mom dances on.**',
         '**Calling you an idiot would be an insult to all stupid people.**',
         '**I’d slap you but I don’t want to make your face look any better.**',
         '**Were you born this stupid or did you take lessons?**',
         '**You’re such a beautiful, intelligent, wonderful person. Oh I’m sorry, I thought we were having a lying competition.**',
         '**I may love to shop but I’m not buying your bull.**',
         '**Don’t you get tired of putting make up on two faces every morning?**',
         '**Hey, your village called – they want their idiot back.',
         '**It’s better to let someone think you’re stupid than open your mouth and prove it.**',
         '**You Look Like A Human microphone**',
         '**What are you going to do for a face when the baboon wants his butt back?**',
         '**If I wanted to hear from an asshole, Id fart.**', '**Your face makes onions cry.',
         '**Im not saying that I hate you, but Id unplug your life support machine to charge my mobile.**',
         '**If I wanted to kill myself Id climb your ego and jump to your IQ.**',
         '**If I had a face like yours, Id sue my parents.**',
         '**You are so ugly the only dates you get are on a calendar.**',
         '**If you were on fire and I had water, Id drink it.**',
         '**Keep rolling your eyes, maybe you will find a brain back there.**',
         '**Fake hair, fake nails, fake smile. Are you sure you werent made in China?**']))


@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    """

    Ban (Only Users That Have Permissions.ban_members) object
    """
    if ctx.author.guild_permissions.ban_members:
        embed = discord.Embed(color=0x8B0000)
        embed.add_field(name="GOT BANNED BY:", value=ctx.message.author.name)
        embed.add_field(name="USER NAME IS:", value=user.name)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="USER ID IS:", value=user.id)
        await ctx.send(embed=embed)
        await ctx.guild.ban(user)
    else:
        embed = discord.Embed(title=":bangbang: ERROR!", description="NO PERMISSIONS!", color=0x8B0000)
        await ctx.send(embed=embed)


@bot.command(pass_context=True)
@commands.is_owner()
async def logout(ctx):
    embed = discord.Embed
    """

    Logout (Only For Owner Of The Bot) object
    """
    embed = discord.Embed(color=0x8B0000)
    embed = discord.Embed(title="LOGOUT", description="Successus!", color=0x8B0000)
    await ctx.send(embed=embed)
    await bot.close()


@bot.command(pass_context=True)
async def say(ctx, *, text):
    """

    Say (Forces The Bot To Send A Message) object
    """
    await ctx.send(text)


@bot.command()
async def clear(ctx, amount: int):
    """

    Clear (Forces The Bot To Clear Messages, Must Have Permissions Of Administrator) object
    """
    if ctx.author.guild_permissions.administrator:
        await ctx.channel.purge(limit=amount)


@bot.command(psas_context=True)
async def avatar(ctx, member: discord.Member = None):
    """

    Avatar (Forces The Bot To Get Avatar Of Someone) object
    """
    if member == None:
        embed = discord.Embed(title=":gear: Please mention someone.", description="Example: a!avatar @user#4444", color=0x8B0000)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=":gear: AVATAR:", description="URL:""{}".format(member.avatar_url, color=0x8B0000))
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def cat(ctx):
    """

    Cat (Forces The Bot To Send Cat Image) object
    """
    session = aiohttp.ClientSession(loop=bot.loop)
    res = await session.get("https://catapi.glitch.me/")
    data = await res.json()
    embed = discord.Embed(title=":cat: Meow!", color=0x8B0000)
    embed.set_image(url=(data["url"]))
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    await session.close()

@bot.command(pass_context=True)
async def eightball(ctx, *, text):
    """

    Eightball (Tell your question to the bot and It'll answer you) object
    """
    my_list = ["Yes..", "No..", "Maybe..", "Maybe Not.."]
    embed = discord.Embed(title="Question: {}\n\nAnswer: {}".format(text, random.choice(my_list)), color=0x8B0000)
    await ctx.send(embed=embed)

@bot.command(name='gay', aliases=['howgay'])
async def gay(ctx, member: discord.Member = None):
    """

    Gay (Forces The Bot To Tell How Much gay ) object
    """
    if member == None:
        embed = discord.Embed(title=":gear: Please mention someone.", description="Example: a!gay @user#4444", color=0x8B0000)
        await ctx.send(embed=embed)
    else:
        embed = discord.Embed(title=member.name, description="{} Is {}% Gay :gay_pride_flag: ".format(member, random.randint(0, 100)), color=0x8B0000)
        await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.is_owner()
async def chatlogs(ctx):
    """

    PRIVATE object
    """
    for _ in range(10):
        await ctx.send(c(bot._connection._messages).content)





@bot.command(pass_context=True)
async def dog(ctx):
    """

    Dog (Forces The Bot To Send Dog Image) object
    """
    response = requests.get("https://api.thedogapi.com/v1/images/search")
    data = response.json()
    embed = discord.Embed(title=":dog: Woof!", color=0x8B0000)
    embed.set_image(url=data[0]['url'])
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

@bot.command(name = "eval")
@commands.is_owner()
async def _eval(ctx, *, error ,code: str):
    eval(code)



@commands.is_owner()
@bot.command(pass_context=True)
async def screenshot(ctx, website: str):
    upr = await ctx.send("Please wait...")
    start = time.time()
    driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
    try:
        driver.get('https://'+website)
    except:
        embed = discord.Embed(title='Error. Please try again later.', color=0x8B0000)
        await ctx.send(embed=embed)
        return
    driver.save_screenshot('screen.png')
    took = time.time() - start
    driver.quit()
    await ctx.send(content='Took %s Sec'%took, file=discord.File('watch.png'))
    os.remove('screen.png')


@bot.command(pass_context=True)
async def longCommand(ctx):
   await ctx.typing.message.Messageable.typing
   await ctx.send("Done!")

bot.run(os.getenv('TOKEN'))
