class script(object):
    START_TXT = """Chibai le {},
    
Kei hi Mizo ṭawnga lehlin movie zawnna Bot ka ni e, keima kaltlang in Mizo ṭawng a lehlin movie te i zawng thei ang. A hmasa ber ah chuan a hnuaia <b>Helpline</b> tih button khu hmet la kha mi group kha join phawt rawh, kha group kha min hmandan a harsatna emaw keimah a felhlelh awm te i thlen na tur ani. Chuan chumi zawh ah chuan <b>Help</b> tih khu min hman dan i hriat theih na'n i hmet leh dawn nia.\n\nHun hman nuam le😊"""
    HELP_TXT = """Min hman dan tur chu tih ngai i tih kim tawh chuan i movie en duh hming kha min thawn tawp rawh, chuan button ka lo thawn che anga, tah khan i duh i hmet leh anga, i hmeh ang apiang kha ka lo thawn ang che, movie zawng zawng erawh ka database ah a awmloa i duh i hmuh loh pawh in a tihdan tur ka lo thawn leh mai ang che, chuan button thlan tur tekha next leh back theih anih kha aw.\n\nMovie hming min thawn tawp lo pawh in tihdan ala awm a, chu chu Inline mode ani, ka profile en la ka username i hmu thei ang, ka username chu @mzmvbot tih ani, kha kha i message type na type box ah khan type la, space vawikhat hmet zeuh la, movie hming kha i type leh dawn nia, chuan i message type na chung ah khan file alo lang anga, tah khan i duh thlan mai tur, file kha result a tam pawh in tuai chhoh khan a dang a tuai chhuah theih aw.\n\n<b>A tihdan:</b> <code>@mzmvbot Chuck</code>\n\nMovie hi request theih ani, command hman tur ania, chu chu <code>/req</code> tih ani, command zawh ah i request tur dah mai tur.\n\n<b>A tihdan:</b> <code>/req Merlin ka lo request e</code>\n\nMin hman dan hi a video a en i duh chuan a hnuaia <b>Tutorial</b> tih button khu hmet la, tah khan min hman dan video en tur alo awm ang, video a en khan hriatthiam a awl zawk ang."""
    ABOUT_TXT = """● Hming: Mizo Movies
● Siamtu: RSR
● Version: 1.0
● Database: Mongo DB"""
    SOURCE_TXT = """<b>NOTE:</b>
- Eva Maria is a open source project. 
- Source - https://github.com/EvamariaTG/EvaMaria  

<b>DEVS:</b>
- <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/EvaMariaBot)</code>

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
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
• /id - <code>get id of a specifed user.</code>
• /info  - <code>get information about a user.</code>
• /imdb  - <code>get the film information from IMDb source.</code>
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
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝚄𝚂𝙴𝚁𝚂: <code>{}</code>
★ 𝚃𝙾𝚃𝙰𝙻 𝙲𝙷𝙰𝚃𝚂: <code>{}</code>
★ 𝚄𝚂𝙴𝙳 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱
★ 𝙵𝚁𝙴𝙴 𝚂𝚃𝙾𝚁𝙰𝙶𝙴: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
    
ID - <code>{}</code>
Name - {}
"""
