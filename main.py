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
@bot.command()
async def soyle(ctx):
    mesaj = random.choice(mesaj1)
    await ctx.send(mesaj)
@bot.command()
async def bagis(ctx):
    await ctx.send("Tema:https://www.tema.org.tr/ , Ağaçlandırma Adına Çalışma Derneği : https://www.agacdernegi.org/")
@bot.command()
async def yardim(ctx):
    await ctx.send('"$soyle" yazarak çalıştırabilirsin :)')
bot.run("MTEzMDE3MzQyMTM3Mjg1NDQ4Mg.GBog6C.JHXu71xumFU03XAN-JZLUzFGrlHHPFs_JC29Ew")