import discord, os
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} Online di FzSTORE!")

@bot.event
async def on_member_join(member):
    channel_id = int(os.getenv("WELCOME_ID"))
    channel = bot.get_channel(channel_id)
    if not channel: return
    embed = discord.Embed(
        title="WELCOME TO FzSTORE!",
        description=f"Halo {member.mention} !!\n\nSelamat datang di server **FzSTORE**\n\n> 📜 Baca rules\n> 🎭 Ambil role\n> 🛒 Cek produk\n\nMember ke-#{member.guild.member_count}",
        color=0x2B2D31
    )
    embed.set_thumbnail(url=member.display_avatar.url)
    await channel.send(content=member.mention, embed=embed)

bot.run(os.getenv("TOKEN"))