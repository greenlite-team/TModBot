import disnake
from disnake.ext import commands
from colorama import Style, Fore
from datetime import datetime, timedelta

class moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.has_permissions(manage_channels=True)
    @commands.slash_command(description="Set channel slowmode in seconds")
    async def slow(self,inter,
    channel: disnake.TextChannel = commands.Param(description="Any text channel"), 
    seconds: int = commands.Param(ge=0, le=21600, description="Maximum 21600 seconds (6h), 0 to disable slowmode")):
        await channel.edit(reason=f"Set by {inter.author}", slowmode_delay=seconds)
        if seconds > 0:
            await inter.send(f"Set slowmode for <#{channel.id}> to `{seconds}` seconds")
        else:
            await inter.send(f"Removed slowmode for <#{channel.id}>")
        print(f'{Fore.LIGHTCYAN_EX}[{datetime.now()}] [MODACT] - {inter.author} set slowmode to {seconds}s in channel #{channel} on {inter.guild}{Style.RESET_ALL}')

    @commands.has_permissions(moderate_members=True)
    @commands.slash_command(description="Timeout a member for X minutes")
    async def timeout(self,inter,
    user: disnake.Member = commands.Param(description="A member to timeout; cannot be an Administrator or the Server Owner"),
    minutes: int = commands.Param(ge=1,le=40320,description="The amount of minutes to timeout a member for; cannot be more than 40320"),
    reason: str = commands.Param(max_length=473,description="Reason for the timeout (shows up in Audit Log)")): # the reason for 473 characters is: discord username length = 32, #+denominator = 5, :+space character = 2. 512-39=474
        if user.guild_permissions.administrator:
            await inter.send("Cannot timeout member: is an Administrator", ephemeral=True)
        elif inter.guild.owner == user:
            await inter.send("Cannot timeout member: is the Server Owner", ephemeral=True)
        else: 
            await user.timeout(duration=minutes*60,reason=f"{inter.author}: {reason}")
            ts = round(datetime.timestamp(datetime.now() + timedelta(minutes=minutes)))
            await inter.send(f"Timed out {user.mention} for `{minutes}` minute(s) until <t:{ts}:f>")
            print(f'{Fore.LIGHTCYAN_EX}[{datetime.now()}] [MODACT] - {inter.author} timed out {user} for {minutes}min on {inter.guild}{Style.RESET_ALL}')

    @slow.error
    async def slow_error(self,inter,error):
        if isinstance(error, commands.MissingPermissions):
            await inter.send("This command requires the `Manage Channels` permission",ephemeral=True)

    @timeout.error
    async def timeout_error(self,inter,error):
        if isinstance(error, commands.MissingPermissions):
            await inter.send("This command requires the `Timeout Members` permission",ephemeral=True)
    
def setup(bot):
    bot.add_cog(moderation(bot))