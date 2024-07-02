import requests
import discord
from discord import app_commands 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
from Squadinfo import Scrape

guildtoken = 1196120408638902272

tenorapi = 'AIzaSyATRda5vY40IDN8MiuwNdK1vhk2Gr4WDjc'


class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False 

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync(guild = discord.Object(id = guildtoken)) 
            self.synced = True
        print(f"We have logged in as {self.user}.")

    async def fetch_gif(self):
        gif_url = "https://tenor.com/view/ooo-you-like-boys-like-boys-oooooo-you-like-boys-boykisser-gif-27678252"
        return gif_url

client = aclient() 

tree = app_commands.CommandTree(client)
@tree.command(guild = discord.Object(id = guildtoken), name = 'hello', description='Hi :3') 
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hello there UwU", ephemeral = False) 

@tree.command(guild = discord.Object(id = guildtoken), name = 'kissboys', description = 'You like kissing boys dont you?')
async def slash2(interaction: discord.Interaction):
    gif_url = await client.fetch_gif()
    await interaction.response.send_message(f"\n{gif_url}", ephemeral = False)

@tree.command(guild = discord.Object(id = guildtoken), name = 'owner', description = 'Quite explanatory')
async def slash2(interaction: discord.Interaction):
    em = discord.Embed(title = 'Owner', description = 'I am the property of Red Penguin Interactive, partnership with FEN1X Squadron')
    await interaction.response.send_message(embed = em, ephemeral = False)
    
@tree.command(guild = discord.Object(id = guildtoken), name = 'sqb-score', description = 'War Thunder Squadron score track')
async def slash2(interaction: discord.Interaction):
    await interaction.response.defer()
    data = Scrape.search()
    em1 = discord.Embed(title = 'Squadron points', description = data, color = 0x00ffff )
    await interaction.followup.send(embed = em1, ephemeral = False)

@tree.command(guild = discord.Object(id = guildtoken), name = 'good-job', description = 'A job well done')
async def slash2(interaction: discord.Interaction):
    gif_url = 'https://tenor.com/view/pats-gif-19157129'
    await interaction.response.send_message(f"\n{gif_url}", ephemeral = False)


client.run('MTEwMzAzNDMzNjY5MDg0Nzg3NQ.GXruQ7.FE7jbtgX7T2R6zwjpu1IyMP0spraG7m-yY5avc')