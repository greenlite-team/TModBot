# <img src="https://i0.wp.com/www.alphr.com/wp-content/uploads/2021/03/How-to-Make-Someone-a-Mod-in-Twitch-scaled.jpg" style="width:32px"> TModBot [BETA]

<a href="https://discord.gg/RNSSJatNbq"><img src="https://img.shields.io/discord/883778577609412660?label=support"></a>
<a href="https://disnake.dev/"><img src="https://img.shields.io/github/v/release/DisnakeDev/disnake?label=disnake"></a>
![GitHub](https://img.shields.io/github/license/greenlite-team/TModBot)

A Discord bot for moderation purposes, inspired by the Twitch moderation commands.

Currently in Beta, as few more projects need to be finished, and Discord already contains good enough replacements for some moderation commands (such as /kick and /ban).

# Requires
- **disnake v2.6** (currently in dev), as it contains the `max_length` parameter for string inputs.
- **colorama** for colorful logging

# Setup
Create a `env.py` file in the root folder of the project, and insert the following code into the file:
```py
TOKEN = "Your Discord application token"
TEST = True
```
The `TOKEN` variable is used as your bot login, while the `TEST` variable is used for restricting your commands for certain servers.

# Support

For any support surrounding the bot, join our [Discord Server](https://discord.gg/RNSSJatNbq) and drop a message in `#support`, I respond in English and Russian.