import discord
from discord.ext import commands
import asyncio

TOKEN = 'MTE4ODM4Nzg0NzE3MDk2NTYyNA.G0vGCj.rpnloLTL74zHHhyhFKFauiNyxzzTsTlU6F44lM'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

stop_flag = False  # Флаг для остановки действий

async def perform_action_1(guild, guild_id_input):
    global stop_flag

    # Удаление всех категорий и каналов на сервере
    for category in guild.categories:
        await category.delete()
    for channel in guild.channels:
        await channel.delete()

    # Запрос ID сервера
    guild_id = int(guild_id_input)
    guild = bot.get_guild(guild_id)

    if not guild:
        print("Сервер не найден.")
        return

    # Создание категории и каналов
    category_announcements = await guild.create_category('announcements')

    # Права доступа для категории announcements
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=True, send_messages=False),
        guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True)
    }

    channel_news = await category_announcements.create_text_channel('News', overwrites=overwrites)
    channel_tickets = await category_announcements.create_text_channel('Tickets', overwrites=overwrites)

    category_general = await guild.create_category('general')
    channel_general = await category_general.create_text_channel('general')
    channel_find_team = await category_general.create_text_channel('find team')
    voice_channels = [f'Voice {i}' for i in range(1, 5)]
    for vc in voice_channels:
        await category_general.create_voice_channel(vc)

    print(f'Запуск удаления и создания категорий и каналов выполнен на сервере {guild.name}.')
    stop_flag = False  # Сброс флага

async def create_templates_menu(guild):
    global stop_flag

    while True:
        print("Выберите тип шаблона:")
        print("1. Запуск удаления и создания категорий и каналов")
        print("2. Краш")
        print("3. Сервер трейдов роблокс")
        print("4. Назад")

        action = input("Введите число (1-4): ")

        if action == "1":
            await perform_action_1(guild, "")
        elif action == "2":
            await create_crash_template(guild)
        elif action == "3":
            await create_roblox_trade_template(guild)
        elif action == "4":
            await main_menu(guild)
        else:
            print("Неверный выбор. Выход.")
            await bot.close()

async def create_roblox_trade_template(guild):
    # Реализуйте создание сервера трейдов роблокс
    pass

async def main_menu(guild):
    global stop_flag

    while True:
        print("Выберите действие:")
        print("1. Запуск удаления и создания категорий и каналов")
        print("2. Создать категорию")
        print("3. Создать канал")
        print("4. Переименовать канал")
        print("5. Удалить канал")
        print("6. Удалить категорию")
        print("7. Удалить сообщение")
        print("8. Удалить все каналы и категории")
        print("9. Написать сообщение")
        print("10. Остановить действие")
        print("11. Выход")
        print("12. Шаблоны")

        action = input("Введите число (1-12): ")

        if action == "1":
            await perform_action_1(guild, "")
        elif action == "2":
            await create_category(guild)
        elif action == "3":
            await create_channel(guild)
        elif action == "4":
            await rename_channel(guild)
        elif action == "5":
            await delete_channel(guild)
        elif action == "6":
            await delete_category(guild)
        elif action == "7":
            await delete_message(guild)
        elif action == "8":
            await delete_all_channels_and_categories(guild)
        elif action == "9":
            await send_message(guild)
        elif action == "10":
            stop_flag = True  # Установка флага остановки
        elif action == "11":
            await bot.close()
        elif action == "12":
            # Вызывать create_crash_template(guild) только если уже было написано "12"
            template_action = input("Введите число для шаблона (1-3): ")
            if template_action == "1":
                await create_crash_template(guild)
            elif template_action == "2":
                await create_roblox_trade_template(guild)
            elif template_action == "3":
                await main_menu(guild)
            else:
                print("Неверный выбор шаблона. Выход.")
                await bot.close()
        else:
            print("Неверный выбор. Выход.")
            await bot.close()

# Добавленные функции

async def create_category(guild):
    # Запрос ID сервера
    guild_id_input = input(f"Введите ID сервера для создания категории на сервере {guild.name}: ")
    guild = bot.get_guild(int(guild_id_input))
    
    if not guild:
        print("Сервер не найден.")
        return

    category_name = input("Введите название категории: ")

    await guild.create_category(category_name)
    print(f"Категория '{category_name}' создана на сервере {guild.name}.")
    await main_menu(guild)

async def delete_channel(guild):
    # Запрос ID сервера
    guild_id_input = input(f"Введите ID сервера для удаления канала на сервере {guild.name}: ")
    guild = bot.get_guild(int(guild_id_input))

    if not guild:
        print("Сервер не найден.")
        return

    channel_id_input = input("Введите ID канала для удаления: ")

    try:
        channel_id = int(channel_id_input)
    except ValueError:
        print("Неверный формат ID канала.")
        await main_menu(guild)
        return

    channel = discord.utils.get(guild.channels, id=channel_id)
    if channel:
        await channel.delete()
        print(f"Канал удален на сервере {guild.name}.")
    else:
        print("Канал не найден.")
    await main_menu(guild)

# ... (остальные функции без изменений)

async def delete_all_channels_and_categories(guild):
    # Запрос ID сервера
    guild_id_input = input(f"Введите ID сервера для удаления всех каналов и категорий на сервере {guild.name}: ")
    guild = bot.get_guild(int(guild_id_input))

    if not guild:
        print("Сервер не найден.")
        return

    for category in guild.categories:
        await category.delete()
    for channel in guild.channels:
        await channel.delete()
    print("Все каналы и категории удалены на сервере {guild.name}.")
    await main_menu(guild)

# ... (остальные функции без изменений)

async def send_message(guild):
    # Запрос ID канала
    channel_id = int(input(f"Введите ID канала для отправки сообщения на сервере {guild.name}: "))
    content = input("Введите текст сообщения: ")

    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(content)
        print("Сообщение отправлено на сервере {guild.name}.")
    await main_menu(guild)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    for guild in bot.guilds:
        await main_menu(guild)

asyncio.run(bot.start(TOKEN))
