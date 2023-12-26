import discord
from discord.ext import commands
import asyncio
from typing import Union
from dateutil.relativedelta import relativedelta

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='?', intents=intents, case_insensitive=True)

# Определение команд
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

def parse_time(time_str):
    multipliers = {'s': 1, 'm': 60, 'h': 3600, 'd': 86400, 'w': 604800, 'M': 2629746, 'y': 31556952}
    unit = time_str[-1]
    if unit in multipliers:
        return int(time_str[:-1]) * multipliers[unit]
    return int(time_str)

@bot.command()
async def mute(ctx, member: discord.Member, duration: str = None):
    try:
        # Создание роли "mute", если её нет
        mute_role = discord.utils.get(ctx.guild.roles, name="mute")
        if not mute_role:
            mute_role = await ctx.guild.create_role(name="mute")
            # Настройка разрешений для роли
            permissions = discord.Permissions(send_messages=False)
            await mute_role.edit(permissions=permissions)

        # Выдача роли "mute"
        await member.add_roles(mute_role)
        await ctx.send(f'{member.mention} был заглушен.')

        if duration is not None:
            seconds = parse_time(duration)
            await asyncio.sleep(seconds)  # Подождать указанное количество секунд
            # Снятие роли "mute" после времени
            await member.remove_roles(mute_role)

    except Exception as e:
        print(f'Error in mute command: {e}')
        await ctx.send(f'Произошла ошибка при выполнении команды.')

@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Пример использования команды: ?mute @пользователь [время] (например, 5m, 1h, 2d)')

@bot.event
async def on_message(message):
    try:
        # Проверка наличия роли "mute"
        mute_role = discord.utils.get(message.guild.roles, name="mute")
        if mute_role and mute_role in message.author.roles:
            await message.delete()

    except Exception as e:
        print(f'Error in on_message event: {e}')

@bot.command()
async def ban(ctx, member: discord.Member, duration: str = None):
    try:
        # Ваш код для бана пользователя
        await ctx.send(f'{member.mention} был забанен.')

        if duration is not None:
            seconds = parse_time(duration)
            await asyncio.sleep(seconds)  # Подождать указанное количество секунд
            # Ваш код для снятия бана после времени

    except Exception as e:
        print(f'Error in ban command: {e}')
        await ctx.send(f'Произошла ошибка при выполнении команды.')

@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Пример использования команды: ?ban @пользователь [время] (например, 5m, 1h, 2d)')

@bot.command()
async def kick(ctx, member: discord.Member):
    try:
        # Ваш код для выгнания пользователя
        await ctx.send(f'{member.mention} был выгнан.')

    except Exception as e:
        print(f'Error in kick command: {e}')
        await ctx.send(f'Произошла ошибка при выполнении команды.')

@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Пример использования команды: ?kick @пользователь')

@bot.command(name='команды')
async def _команды(ctx):
    help_message = '```Примеры использования команд:\n'
    help_message += '?mute @пользователь [время] - Заглушить пользователя на указанное время\n'
    help_message += '?ban @пользователь [время] - Забанить пользователя на указанное время\n'
    help_message += '?kick @пользователь - Выгнать пользователя\n```'
    await ctx.send(help_message)

# Токен вашего бота
bot.run('MTE4ODM4Nzg0NzE3MDk2NTYyNA.G0vGCj.rpnloLTL74zHHhyhFKFauiNyxzzTsTlU6F44lM')
