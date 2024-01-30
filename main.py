import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)
mesaj1 = ["Sık sık tema gibi toprak ve ağaç kurullarına bağış yap.","Yere çöp atma, atanları uyar ve çok israf yapma.",
"Fidan dik.","Işıkları çok yakma","Geridönüşüm ve Atık Azaltma: Atıkları ayrıştırarak geridönüşüme katkıda bulunun, sıfır atık hedefi belirleyin, plastik kullanımını azaltın.",
"Enerji Tasarrufu: LED lambalar kullanarak enerji tüketimini azaltın, elektronik cihazları kullanmadığınızda fişleri çekin, enerji verimliliğini artırmak için izolasyon ve tasarruf önlemleri alın."]
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptım.')
@bot.command
async def on_ready(ctx):
    await ctx.send('Merhaba, "soyle" yazarak kullanabilirsin')
@bot.command()
async def soyle(ctx):
    mesaj = random.choice(mesaj1)
    await ctx.send(mesaj)
bot.run("token")