import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import os

# Configurações do bot
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Agendador
scheduler = AsyncIOScheduler()

# Quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

    # Defina o canal onde a mensagem será enviada
    channel_id = 1274363982999846944  # Substitua pelo ID real do canal do Discord

    # Agendar a mensagem diária às 10:00
    scheduler.add_job(send_daily_message, CronTrigger(hour=16, minute=57), args=[channel_id])
    scheduler.start()

# Função para enviar a mensagem diária
async def send_daily_message(channel_id):
    print('enviando mensagem')
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("bip bop, im a bot, bip boop.")

# Rodar o bot
bot.run(os.getenv('DISCORD_TOKEN'))  # Certifique-se de configurar a variável de ambiente DISCORD_TOKEN
