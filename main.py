import discord
from discord.ext import commands
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='', intents=intents)

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@bot.event
async def on_ready():
    print(f'You have logged in as {bot.user}')

@bot.command()
async def Pot_tanaman_dari_sampah_plastik(ctx):
    img_name = random.choice(os.listdir('1image'))
    with open(f'1image/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)
    await ctx.send("Cara membuatnya:")
    await ctx.send("1. Siapkan Botol plastik bekas, alat pemotong, benang pancing, dan paku")
    await ctx.send("2. Kemudian potong bagian tengahnya dan sampingnya")
    await ctx.send("3. Kemudian lubangi menggunakan paku di sekitar botol plastik")
    await ctx.send("4. Kemudian buat gantungan di atas atau di kedua sisinya untuk potongan botol")
    await ctx.send("5. Kemudian kamu bisa mengisi tanaman didalamnya, lalu gantung pot tersebut")

@bot.command()
async def Batako_dari_sampah_plastik(ctx):
    img_name = random.choice(os.listdir('2image'))
    with open(f'2image/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)
    await ctx.send("Cara membuatnya:")
    await ctx.send("1. Kumpulkan sampah plastik, contohnya plastik kresek, botol plastik, plastik kemasan makanan, sterofoam dan lain-lain")
    await ctx.send('2. Kemudian cuci sampah hingga bersih dari sisa-sisa makanan atau sampah organik lain, lalu keringkan hingga benar-benar kering')
    await ctx.send('3. Kemudian potong sampah plastik sampai menjadi bagian yang lebih kecil')
    await ctx.send('4. Kemudian masukkan potongan sampah plastik kedalam kuali yang tidak terpakai, panaskan hingga meleleh, campurkan dengan bahan lain seperti pasir dan oli bekas(penggunaan oli bekas agar adonan sampah tidak lengket dengan wadahnya), lalu aduk hingga merata')
    await ctx.send('5. Kemudian masukkan adonan sampah ke cetakan batako, ratakan hingga semua sisi terisi, jangan lupa padatkan agar batako tidak berpori-pori')
    await ctx.send('6. Kemudian masukkan cetakan batako kedalam air dan tunggu hingga dingin, jika sudah dingin kamu bisa melepas batako plastik dari cetakannya')
    await ctx.send('7. Kemudian kamu bisa memoles dan mencat batako plastik agar tampilannya lebih bagus')
    await ctx.send('8. Batako siap dipakai')

@bot.command()
async def Tabungan_dari_sampah_plastik(ctx):
    img_name = random.choice(os.listdir('3image'))
    with open(f'3image/{img_name}', 'rb') as f:
        picture = discord.File(f)

    await ctx.send(file=picture)
    await ctx.send("Cara membuatnya:")
    await ctx.send("1. Siapkan botol plastik bekas, alat pemotong dan lem atau lakban")
    await ctx.send("2. Kemudian bersihkan botol plastik hingga bersih")
    await ctx.send("3. Kemudian lem tutup botol agar tidak mudah terbuka")
    await ctx.send("4. kemudian buat lubang untuk tempat memasukkan uang menggunakan alat pemotong, untuk lokasi lubangnya kamu bisa menyesuaikannya dengan seleramu")
    await ctx.send("5. Kamu bisa menghiasnya jika mau")
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################@bot.command()
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################async def on_message(message):
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀    if message.author == bot.user:
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀        return
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀    if message.content.startswith('Bagaimana_cara_membuat'):
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀        await message.channel.send('Apa yang kamu ingin buat?<batako/pot tanaman/tabungan>')
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀            await message.channel.send('2. Kemudian cuci sampah hingga bersih dari sisa-sisa makanan atau sampah organik lain, lalu keringkan hingga benar-benar kering')
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀            await message.channel.send('3. Kemudian potong sampah plastik sampai menjadi bagian yang lebih kecil')
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀            await message.channel.send('4. Kemudian masukkan potongan sampah plastik kedalam kuali yang tidak terpakai')
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀            await message.channel.send('5. a')
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀            await message.channel.send('6. b')
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀            await message.channel.send('7. c')
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀        elif message.contene.startswith('pot tanaman'):
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀            await message.channel.send('a')
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀        elif message.contene.startswith('tabungan'):
##################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################🚀            await message.channel.send('b')

bot.run("Token")