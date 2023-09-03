import discord
from discord.ext import commands
from googletrans import Translator

intents = discord.Intents.default() #burası yeni discord sürümünden sonra lazım 
intents.message_content = True  

bot = commands.Bot(command_prefix='.', intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="THT"))  #bot durum
    print(f'Hazırız {bot.user.name}')#başlayınca alıcağınız mesaj

@bot.command() #comut ekliyoz ilk bölüm ceviri
async def ceviri(ctx, source_lang, target_lang, *, text):
    try:
        ceviri = Translator()
        translated_text = ceviri.translate(text, src=source_lang, dest=target_lang)
        embed = discord.Embed(title="Çeviri Sonucu", color=0x00ff00)
        embed.add_field(name="Kaynak Dil", value=translated_text.src, inline=True)
        embed.add_field(name="Hedef Dil", value=translated_text.dest, inline=True)
        embed.add_field(name="Çeviri", value=translated_text.text, inline=False)
        
        await ctx.send(embed=embed)
    except Exception as e:
        await ctx.send("404")

@bot.command()#ping komutu
async def ping(ctx):
    latency = bot.latency * 1000  
    await ctx.send(f'Ping: {latency:.2f} ms')

@bot.command() #yardim komutu
async def yardim(ctx):
    help_message = (
        "**Çeviri Komutu**:\n"
        "`!translate kaynak_hedef metin` komutunu kullanarak metin çevirisi yapabilirsiniz.\n\n"
        "**Ping Komutu**:\n"
        "`!ping` komutunu kullanarak botun ping süresini öğrenebilirsiniz."
    )
    
    await ctx.send(help_message)

bot.run("MTA0NzE2NzAxNDIwMTk5NTI3Ng.GlNNgM.B1iXbnlRe0bA2KNcepL3wxj4S2zaLTeBRheYWs")



#   MTA0NzE2NzAxNDIwMTk5NTI3Ng.GlNNgM.B1iXbnlRe0bA2KNcepL3wxj4S2zaLTeBRheYWs