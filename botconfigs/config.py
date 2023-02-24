import sys
from pathlib import Path

# set up base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database
DB_FILE = str(BASE_DIR / 'botconfigs' / 'discord_db.db')

# Bot
BOT_PREFIX = '!'

BOT_STATS = {
        'Bot Version': '0.1 beta',
        'Python version': '.'.join(map(str, sys.version_info[:3])),
        'Discord.py Version': '',
        'Total Users': '*Not yet coded*',
        'Total Guilds': '*Not yet coded*',
        'Bot Created': 'February 22, 2023',
        'Bot Developers': {'name': 'Jerson', 'discordId':'729082383826944002'},
}
