import discord
from discord.ext import commands
import asyncio
import random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

recordatorios = [
    "Apaga las luces cuando no las uses 💡.",
    "Usa una botella reutilizable en lugar de plástico 🧴.",
    "Camina o usa bicicleta en lugar de coche 🚶‍♂️🚲.",
    "Separa tu basura para reciclar ♻️.",
    "Reduce el consumo de agua cerrando la llave al cepillarte 🪥🚱."
]

@bot.command()
async def contaminacion(ctx):
    recordatorio = random.choice(recordatorios)
    await ctx.send(f"¡Tu reto ecológico! {recordatorio}")




bot.run("TOKEN")
