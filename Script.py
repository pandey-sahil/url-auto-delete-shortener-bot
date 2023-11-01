import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://omegalinks.in/')
    START_TXT = environ.get("START_TXT", '''<b>ᴋᴏɴɪᴄʜɪᴡᴀ​ {}-ꜱᴀɴ​ 👋🏻
ɪ'ᴍ ɴɪᴄᴏ ʀᴏʙɪɴ ᴀ ꜰɪʟᴇ ꜱʜᴀʀɪɴɢ ʙᴏᴛ
<a href=https://t.me/Uncensored_Hanimes><b>ᴜɴᴄᴇɴꜱᴏʀᴇᴅ ʜᴀɴɪᴍᴇꜱ</b> 😁.</b>''')
    HELP_TXT = """ʜᴇʏᴀ {}
ʏᴏᴜ ᴡᴀɴᴛ ʜᴇʟᴘ ʜᴇʀᴇ ɪᴛ ɪꜱ ᴄʟɪᴄᴋ ʙᴇʟᴏᴡ."""
    ABOUT_TXT = """<b><i>​ᴍʏ ɴᴀᴍᴇ​: <a href=https://t.me/NicoRobinRobot><b>ɴɪᴄᴏ ʀᴏʙɪɴ​</b></a>\n
📝 ​ʟᴀɴɢᴜᴀɢᴇ​ : ᴘʏʀᴏɢʀᴀᴍ\n
📚 ​ꜰʀᴀᴍᴇᴡᴏʀᴋ : ᴘʏᴛʜᴏɴ 3\n
📡 ​ʜᴏsᴛᴇᴅ ᴏɴ : Koyeb\n
📢 ​ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Uncensored_Hanimes><b></b>ᴄʟɪᴄᴋ ʜᴇʀᴇ</a>\n
🌟 ​ᴠᴇʀsɪᴏɴ : ᴠ 4.0\n</b></i>"""
    SOURCE_TXT = """<b>......</b>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and Bot will respond whenever a keyword is found the message

<b>NOTE:</b>
1. Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/UpperDemon)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Search Bot

<b>Commands and Usage:</b>
• /id - <code>get id of a specified user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the movie or series information from IMDb source.</code>
• /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
• /logs - <code>to get the rescent errors</code>
• /stats - <code>to get status of files in db.</code>
• /delete - <code>to delete a specific file from db.</code>
• /users - <code>to get list of my users and ids.</code>
• /chats - <code>to get list of the my chats and ids </code>
• /leave  - <code>to leave from a chat.</code>
• /disable  -  <code>do disable a chat.</code>
• /ban  - <code>to ban a user.</code>
• /unban  - <code>to unban a user.</code>
• /channel - <code>to get list of total connected channels</code>
• /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """ᴛᴏᴛᴀʟ ꜰɪʟᴇꜱ: <code>{}</code>
ᴛᴏᴛᴀʟ ᴜꜱᴇʀꜱ: <code>{}</code>
ᴛᴏᴛᴀʟ ᴄʜᴀᴛꜱ: <code>{}</code>
ᴜꜱᴇᴅ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code> ᴍ𝚒ʙ
ꜰʀᴇᴇ ꜱᴛᴏʀᴀɢᴇ: <code>{}</code> ᴍ𝚒ʙ"""
    LOG_TEXT_G = """#ɴᴇᴡ_ɢʀᴏᴜᴘ
    
<b>᚛› ɢʀᴏᴜᴘ ⪼ {}(<code>{}</code>)</b>
<b>᚛› ᴛᴏᴛᴀʟ ᴍᴇᴍʙᴇʀꜱ ⪼ <code>{}</code></b>
<b>᚛› ᴀᴅᴅᴇᴅ ʙʏ ⪼ {}</b>
"""
    LOG_TEXT_P = """#ɴᴇᴡ_ᴜꜱᴇʀ
    
<b>᚛› ɪᴅ - <code>{}</code></b>
<b>᚛› ɴᴀᴍᴇ - {}</b>
"""
