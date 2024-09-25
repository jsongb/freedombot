import discord
from discord.ext import commands
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
import os

# Configurações do bot
intents = discord.Intents.default()
intents.messages = True
bot = commands.Bot(command_prefix="!", intents=intents)
announce_channel = 1274137747535167600
alchemy_channel = 1274363982999846944

# Agendador
scheduler = AsyncIOScheduler()

# Quando o bot estiver pronto
@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

    # Defina o canal onde a mensagem será enviada
    channel_id = 1274137747535167600  # Substitua pelo ID real do canal do Discord


    # Agendar a mensagem diária às 10:00
    # scheduler.add_job(send_test_message, CronTrigger(hour=16, minute=57), args=[channel_id])

    # hour	minute	task
    # 9  59 tower
    # 18 30 alchemy
    # 2	 0  restart

    # AGENDADOR DA TORRE 10h e 16h
    scheduler.add_job(tower, CronTrigger(hour=13, minute=29), args=[announce_channel])
    scheduler.add_job(tower, CronTrigger(hour=19, minute=29), args=[announce_channel])

    # AGENDADOR DA alquimia 18:30
    scheduler.add_job(alchemy, CronTrigger(hour=21, minute=30), args=[alchemy_channel])

    # AGENDADOR DO RESTART 3:30
    scheduler.add_job(restart, CronTrigger(hour=5, minute=30), args=[announce_channel])

    # AGENDADOR DO RESTART FINALIZADO 3:41
    scheduler.add_job(restart_finished, CronTrigger(hour=6, minute=42), args=[announce_channel])

    # new_auction_items 4h
    scheduler.add_job(new_auction_items, CronTrigger(hour=7, minute=1), args=[announce_channel])

    # new_auction_items 15h
    # scheduler.add_job(new_auction_items, CronTrigger(hour=17, minute=1), args=[announce_channel])

    scheduler.start()

# Função para enviar a mensagem diária
async def send_test_message(channel_id):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send("bip boop, i am a robot, bip boop.")

async def tower(channel_id):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send('''👹🏰 **A Torre de Milhões de bestas vai iniciar em instantes, registre-se e participe! 👹🏰**
        @everyone
        ''')

async def alchemy(channel_id):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send('''🧱🔥 **Já conferiu nossa alquimia de hoje? Confira os itens da alquimia no site https://grandfantasiafreedom.lovestoblog.com **
        @everyone
        ''')

async def restart(channel_id):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send('''🔧⚙️ **O servidor vai reiniciar para a manutenção diária em instantes.** 🔧⚙️
        @everyone
        ''')

async def restart_finished(channel_id):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send('''**Servidor online✅. Aproveite!**
        "@everyone
        ''')


async def new_auction_items(channel_id):
    channel = bot.get_channel(channel_id)
    if channel:
        await channel.send('''**Temos novos itens no leilão!!!**
        @everyone
        ''')

# Rodar o bot
bot.run(os.getenv('DISCORD_TOKEN'))  # Certifique-se de configurar a variável de ambiente DISCORD_TOKEN