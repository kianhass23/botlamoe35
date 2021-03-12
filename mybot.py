# Import discord package
import discord
import random
from discord.ext import commands
import asyncio

# Client bot
client = commands.Bot(command_prefix='.')
client.remove_command('help')
client.warnings = {}# guild_id : {member_id: [count, [[[admin_id, reason]]]}
   




   # DO STUF
    
@client.command(name='purge')
@commands.has_permissions(administrator=True)
async def purge(ctx, amount, arg:str=None):
   await ctx.message.delete()
   await ctx.channel.purge(limit=int(amount))
   message_to_delete = await ctx.send(f'**{amount} MESSAGES HAS BEEN SUCCESSFULLY DELETED**')
   await asyncio.sleep(1)
   await message_to_delete.delete()

@purge.error
async def purge_error(ctx, error):
   if isinstance(error, commands.MissingPermissions):
      await ctx.send('**YOU ARE MISSING PERMISSIONS `ADMINISTRATOR`**')
   elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('**PLEASE MAKE SURE TO INPUT HOW MANY MESSAGES YOU WANT TO DELETE**')



@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx, member: discord.Member=None, *, reason=None):
   if isinstance(error, commands.MissingPermissions):
      await ctx.send('**⭕ YOU ARE MISSING PERMISSIONS `ADMINISTRATOR`**')
   elif isinstance(error, commands.MissingRequiredArgument):
      await ctx.send('**⭕ PLEASE INPUT USERS @**')



@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
 await member.kick(reason=reason)
 await ctx.send(f"{member.mention}**KICKED!:thumbsup:**")

@kick.error
async def kick_error(ctx, error):
   if isinstance(error, commands.MissingPermissions):
      await ctx.send('**⭕ YOU ARE MISSING PERMISSIONS `ADMINISTRATOR`**')
   elif isinstance(error, commands.MissingRequiredArgument):
       await ctx.send('**⭕ PLEASE INPUT USERS @**')

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
 await member.ban(reason=reason)
 await ctx.send(f"{member.mention}**BANNED! :thumbsup:**")

@ban.error
async def ban_error(ctx, error):
   if isinstance(error, commands.MissingPermissions):
      await ctx.send('**⭕ YOU ARE MISSING PERMISSIONS `ADMINISTRATOR`**')
   elif isinstance(error, commands.MissingRequiredArgument):
       await ctx.send('**⭕ PLEASE INPUT USERS @**')


@client.command()
@commands.has_permissions(administrator=True)
async def lockdown(ctx):
   await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
   await ctx.send(ctx.channel.mention +  "**IS NOW IN LOCKDOWN:thumbsup:**")


@lockdown.error
async def lockdown_error(ctx, error):
   if isinstance(error, commands.MissingPermissions):
      await ctx.send('**⭕ YOU ARE MISSING PERMISSIONS `ADMINISTRATOR`**')
   elif isinstance(error, commands.MissingRequiredArgument):
       await ctx.send('**⭕ PLEASE INPUT USERS @**')




@client.command()
@commands.has_permissions(administrator=True)
async def unlock(ctx):
   await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
   await ctx.send(ctx.channel.mention +  "**HAS BEEN UNLOCKED:thumbsup:**")






@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
   role = discord.utils.get(ctx.guild.roles, name="Muted")
   if not member:
      await ctx.send("**PLEASE SPECIFY MEMBER**")
      return
   await member.add_roles(role)
   await ctx.send(f"{member.mention} **MUTED**")

@mute.error
async def mute_error(ctx, error):
   if isinstance(error, commands.MissingPermissions):
      await ctx.send('**⭕ YOU ARE MISSING PERMISSIONS `ADMINISTRATOR`**')
   elif isinstance(error, commands.MissingRequiredArgument):
       await ctx.send('**⭕ PLEASE INPUT USERS @**')

@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
   role = discord.utils.get(ctx.guild.roles, name="Muted")
   if not member:
      await ctx.send("**⭕ YOU ARE MISSING PERMISSIONS `ADMINISTRATOR`**")
      return
      await member.remove_roles(role)
      await ctx.send(f"{member.mention} **UNMUTED**")


@unmute.error
async def unmute_error(ctx, error):
   if isinstance(error, commands.MissingPermissions):
      await ctx.send('**⭕ YOU ARE MISSING PERMISSIONS `ADMINISTRATOR`**')
   elif isinstance(error, commands.MissingRequiredArgument):
       await ctx.send('**⭕ PLEASE INPUT USERS @**')
      

   await ctx.send(embed=helpembed)



@client.command()
async def ping(ctx):
   await ctx.send('f**PONG!**')

@client.command()
async def help(ctx):
   helpembed=discord.Embed(title='**[🤖] BOT COMMANDS**', description='**CODED BY SCARECROW**', colour=random.randint(0, 0xffffff))
   helpembed.add_field(name='[⚠️] BAN MEMBER', value='**cmd = .ban**')
   helpembed.add_field(name='[👾] KICK MEMBER', value='**cmd = .kick**')
   helpembed.add_field(name='[🤐] MUTE MEMBER', value='**cmd = .mute**')
   helpembed.add_field(name='[✔️] PURGE MESSAGES..', value='**cmd = .purge (AMOUNT)**')
   helpembed.add_field(name='[🦷] LOCK CHANNEL.', value='**cmd = !lockdown**')
   helpembed.add_field(name='[🩸] UNLOCK CHANNEL.', value='**cmd = !unlock**')
   helpembed.add_field(name='[☠️] ADDING MORE..', value='**cmd = NONE**')

   await ctx.send(embed=helpembed)


# Run the client on the server
client.run('ODE5MTA5OTUxNTgxNDU0MzU2.YEh1lg.XhRE3p2pR-kVWduB7bRZ4D-oiwM')
