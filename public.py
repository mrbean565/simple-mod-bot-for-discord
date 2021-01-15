import discord
from discord.ext import commands
token = "bot token goes here"
client = commands.Bot(command_prefix='prefix goes here')

#remove help command (default)
client.remove_command('help')

@client.event
async def on_ready():
    print("My body is ready")
    await client.change_presence(activity=discord.Game(name='Goated 🐐'))


#help command option 1 // below 

@client.command()
async def help(ctx):
   await ctx.send("custom help can go here")




@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')



@client.command(pass_context=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked for the following reason: {reason}')


@client.command(pass_context=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned for the following reason: {reason}')


@client.command(pass_context=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned {user.mention}")


@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

client.run(token)
