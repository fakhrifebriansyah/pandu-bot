import discord
from discord.ext import commands

class MyCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.Cog.listener()
    async def on_ready(self):
        print("MyCog.py is online")
        
    @commands.command()
    async def embed(self, ctx):
        embed_message = discord.Embed(title="MyCog Test", description="Description MyCog Test Embed", colour=discord.Color.green())
        
        embed_message.set_author(name=f"Requested by {ctx.author.mention}", icon_url=ctx.author.avatar)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url=ctx.guild.icon)
        embed_message.add_field(name="Field Name", value="Field Value", inline=False)
        embed_message.set_footer(text="This is the Footer", icon_url=ctx.author.avatar)
        
        await ctx.send(embed = embed_message)
        
        
async def setup(client):
    await client.add_cog(MyCog(client))