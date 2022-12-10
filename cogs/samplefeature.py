import nextcord
from nextcord.ext import commands

class SampleFeature(commands.Cog):

    def __inint__ ( self , bot ) :
        self.bot = bot



    #Events

    @commands.Cog.listener()
    async def on_ready (self) :
        print('Bot is online and sample feature is active')


    #Commands

    @commands.command()
    async def psf ( self , ctx ) :
        await ctx.send('Sample Feature is Active') # ping sample feature


def setup( bot ):
    bot.add_cog(SampleFeature(bot))
    
