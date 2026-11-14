import discord
from discord import app_commands
from discord.ext import commands

TOKEN = "YOUR_BOT_TOKEN_HERE"

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"Parlay Intelligence online as {bot.user}")

@bot.tree.command(name="build", description="Build a parlay")
@app_commands.describe(legs="Number of legs", style="Build style")
async def build(interaction: discord.Interaction, legs: int, style: str = "Balanced"):
    await interaction.response.send_message(
        f"🧠 **Parlay Intelligence**\n"
        f"Style: {style}\n"
        f"Requested legs: {legs}\n"
        "Pick analysis is not connected yet. We're building that next."
    )

bot.run(TOKEN)
