import discord
from botconfigs.config import BOT_PREFIX, DB_FILE
from botconfigs.database import Database
from discord.ext import commands

class WordsCounterCog(commands.Cog):

    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def test(self, ctx, *args):

        with Database(DB_FILE) as db:
            exit