import discord
from discord.ext import commands
token = "bot token goes here"
client = commands.Bot(command_prefix='prefix goes here')

#remove help command (default)
client.remove_command('help')

@client.event
async def on_ready():
    print("My body is ready")
    await client.change_presence(activity=discord.Game(name='custom status'))



# welcome message
@client.event
async def on_member_join(member):
       # will do both simple single line msg and embed
       # singel line welcome message. 
       welcome_channel = client.get_channel() # put channel id in brackets.
       await welcome_channel.send(f"Hey {member.mention} welcome to server name")    
       # embed form
       welcome_em = discord.Embed(title=f"Welcome {member.mention}", description="Add anything u want here", color=0xFF0000) # feel free to change the color to whatever u like i like https://htmlcolorcodes.com/ but make sure to put 0x{hexcode}
       welcome_em.set_thumbnail(url=member.avatar_url)
       welcome_channel_for_embed = client.get_channel() # put channel id in brackets.
       await welcome_channel_for_embed.send(embed=welcome_em)


#  give roles to new members
@client.event
async def on_member_join(member):
 # may need to install a module. 
 role = discord.utils.get(member.server.roles, name="Role name")
 await member.add_roles(role)

#help command option 1 // below 

@client.command()
async def help(ctx):
   await ctx.send("custom help can go here")

#find out the servers ping / connection latency to the discord servers
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')


# use this command to kick users 
@client.command(pass_context=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked for the following reason: {reason}')

#use this to ban members / users
@client.command(pass_context=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned for the following reason: {reason}')

#use this to unban banned members
@client.command(pass_context=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"unbanned {user.mention}")

# ust this to change nicknames of users. In your discord server. 
@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, *, nick):
    await member.edit(nick=nick)
    await ctx.send(f'Nickname was changed for {member.mention} ')

client.run(token)
