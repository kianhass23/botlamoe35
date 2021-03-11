# Import discord package
import discord
import random
from discord.ext import commands
import asyncio

# Client bot
client = commands.Bot(command_prefix='.')
client.snipe_messages = {}
client.remove_command('help')

@client.command(name='yo')
async def version(context):




   # DO STUFF

   general_channel = client.get_channel(817706086484279326)
   await general_channel.send('e')

@client.command(name='purge')
@commands.has_permissions(administrator=True)
async def purge(ctx, amount, *, arg:str=None):
     await ctx.message.delete()
     await ctx.channel.purge(limit=int(amount))
     message_to_delete = await ctx.send(f'{amount} **MESSAGE HAVE BEEN DELETED👍**')
     await asyncio.sleep(1)
     await message_to_delete.delete()


@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
 await member.kick(reason=reason)
 await ctx.send(f"{member.mention}**KICKED!:thumbsup:**")

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
 await member.ban(reason=reason)
 await ctx.send(f"{member.mention}**BANNED! :thumbsup:**")



@client.command()
async def mute(ctx, member: discord.Member=None):
   role = discord.utils.get(ctx.guild.roles, name="Muted")
   if not member:
      await ctx.send("**PLEASE SPECIFY MEMBER**")
      return
   await member.add_roles(role)
   await ctx.send(f"{member.mention} **MUTED**")

@client.command()
async def umute(ctx, member: discord.Member=None):
   role = discord.utils.get(ctx.guild.roles, name="Muted")
   if not member:
      await ctx.send("SEXME")
      return
   await member.remove_roles(role)
   await ctx.send(f"{member.mention} **UNMUTED**")
      

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
   helpembed.add_field(name='[☠️] ADDING MORE..', value='**cmd = NONE**')

   await ctx.send(embed=helpembed)


# Run the client on the server
client.run('ODE5MTA5OTUxNTgxNDU0MzU2.YEh1lg.mtC50qTjNPfh1Tg6RaqZMVs7d4c')