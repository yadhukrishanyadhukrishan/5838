class script(object):
    START_TXT = """ð·ðīðŧðū {},
ðžð ð―ð°ðžðī ðļð <a href=https://t.me/{}>{}</a>, ðļ ðēð°ð― ðŋððūððļðģðī ðžðūððļðīð, ðđððð ð°ðģðģ ðžðī ððū ððūðð ðķððūððŋ ð°ð―ðģ ðžð°ðšðī ðžðī ð°ðģðžðļð―.. ðð·ðīð― ððīðī ðžð ðŋðūððīðð âĨïļâĨïļðĨ"""
    HELP_TXT = """ð·ðīð {}
ð·ðīððī ðļð ðð·ðī ð·ðīðŧðŋ ðĩðūð ðžð ðēðūðžðžð°ð―ðģð."""
    ABOUT_TXT = """âŪ ðžð ð―ð°ðžðī: {}
âŪ ðēððīð°ððūð: <a href=https://t.me/moviespot00100>ðžs ððŋðģð°ððīð</a>
âŪ ðŧðļðąðð°ðð: ðŋðððūðķðð°ðž
âŪ ðŧð°ð―ðķðð°ðķðī: ðŋððð·ðūð― ðđ
âŪ ðģð°ðð° ðąð°ððī: ðžðūð―ðķðū ðģðą
âŪ ðąðūð ððīðððīð: ð·ðīððūðšð
âŪ ðąððļðŧðģ ððð°ððð: v1.0.2 [ ðąðīðð° ]"""
    DONATION_TXT = """<b>ððĻð§ðð­ðĒðĻð§ & ðððĒð ððŦðĻðĶðĻð­ðĒðĻð§</b> 

âšâš <b>ððĻð§ðð­ðĒðĻð§</b>

âŠž <b>ððĻðŪ ððð§ ððĻð§ðð­ð ðð§ðē ððĶðĻðŪð§ð­ ððĻðŪ ðððŊð ðģ. 
<b>âââââââââá Payment Methods áâââââââââ
âŪ Google play redeem code
_ððĻð§ð­ððð­ ðð ððĻðŦ ðð§ðĻð° ðððĻðŪð­ ððĄð ðððēðĶðð§ð­ ðð§ððĻ_
ââââââââââââá <a href=https://t.me/zinan00100><b>zinan tech 2.O</b></a> áââââââââââââ

âšâš <b>ðððĒð ððŦðĻðĶðĻð­ðĒðĻð§</b>

âŠž <b>ððĻð§ð­ððð­ ðð ððĒð­ðĄ ððĻðŪ ððĻð§ð­ðð§ð­ ððĄðĒððĄ ððĻðŪ ððð§ð­ ððĻ ððŦðĻðĶðĻð­ð . 
<b>âââââââââá Payment Methods áâââââââââ
âŪ Google play redeem code
_ððĻð§ð­ððð­ ðð ððĒð­ðĄ ððĻðŪðŦ ððĻð§ð­ðð§ð­ ðð§ð ðð§ðĻð° ðððĻðŪð­ ððĄð ðððēðĶðð§ð­ ðð§ððĻ_
ââââââââââââá <a href=https://t.me/zinan00100><b>zinan tech 2.O</b></a> áââââââââââââ"""

    PROMOTION_TXT = """<b>ã ðððĒð ððŦðĻðĶðĻð­ðĒðĻð§ ã</b>

âŠž <b>ððĻð§ð­ððð­ ðð ððĒð­ðĄ ððĻðŪ ððĻð§ð­ðð§ð­ ððĄðĒððĄ ððĻðŪ ððð§ð­ ððĻ ððŦðĻðĶðĻð­ð . 
<b>âââââââââá Payment Methods áâââââââââ
âŪ ððžðžðīðđðēðĢðŪð
âŪ ðĢðŪðððš
âŪ ðĢðĩðžðŧðēðĢðē
âŪ ðĢðŪððĢðŪðđ
_ððĻð§ð­ððð­ ðð ððĒð­ðĄ ððĻðŪðŦ ððĻð§ð­ðð§ð­ ðð§ð ðð§ðĻð° ðððĻðŪð­ ððĄð ðððēðĶðð§ð­ ðð§ððĻ_
ââââââââââââá <a href=https://t.me/zinan00100><b>zinan tech 2.O</b></a> áââââââââ"""

    WHOIS_TXT ="""<b>WHOIS MODULE</b>
Note:- Give a user details
âĒ/whois :-give a user full details"""
    FUN_TXT ="""<b>Gáīáīáīs</b> 
    
<b>ðē NOTHING MUCH JUST SOME FUN THINGS</b>
tðð ðððð ðŪðð: 
ðĢ. /dice - Roll The Dice 
ðĪ. /Throw ðð /Dart - ðģð ðŽðšððū Drat 
3. /Runs - Jokes 
4. /Goal or /Shoot - To Make A Goal Or Shoot
5. /luck or /cownd - Spin the Lucky"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message

<b>NOTE:</b>
1. eva maria should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âĒ /filter - <code>add a filter in chat</code>
âĒ /filters - <code>list all the filters of a chat</code>
âĒ /del - <code>delete a specific filter in chat</code>
âĒ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    SONG_TXT = """<b>ðžSong Downloadðž</b>
Song Download Module, For Those Who Love Music

<b>ð Command ð</b>

- /song [Song Name] - To Download Music ð

<b>ðUsageð</b>
- Can Be Used By Everyone
- Works in bot pm

Made By <a href=https://t.me/+veUIdIW2CQ5mOGU5>ðð ððĐððð­ððŽ</a>"""
    PIN_TXT ="""<b>PIN MODULE</b>
<b>Pin :</b>

<b>All The Pin Related Commands Can Be Found Here; Keep Your Chat Up To Date On The Latest News With A Simple Pinned Message!</b>

<b>ð Commands & Usage:</b>

â /pin :- Pin The Message You Replied To Message To Send A Notification To Group Members
â /unpin :- Unpin The Current Pinned Message. If Used As A Reply, Unpins The Replied To Message"""
    PASTE_TXT = """Help: <b>Paste</b>

Paste some texts or documents on a website!

<b>Commands and Usage:</b>

âĒ /paste [text] - paste the given text on Pasty

<b>NOTE:</b>

âĒ These commands works on both pm and group.
âĒ These commands can be used by any group member."""
    GTRANS_TXT = """Help: <b> TTS ðĪ module:</b>

Translate text to speech

<b>Commands and Usage:</b>

âĒ /tts <text> : convert text to speech

<b>NOTE:</b>

âĒ IMDb should have admin privillage.
âĒ These commands works on both pm and group.
âĒ IMDb can translate texts to 200+ languages."""
    PINGS_TXT ="""<b>ð Ping:</b>

Helps you to know your ping ðķðžââïļ

<b>Commands:</b>

âĒ /alive - To check you are alive.
âĒ /help - To get help 
âĒ /ping - To get your ping 
âĒ /repo - Source Code. 

<b>ðđUsageðđ :</b>

âĒ This commands can be used in pms and groups
âĒ This commands can be used buy everyone in the groups and bots pm
âĒ Share us for more features"""
    TELE_TXT = """<b>âŦïļHELP: TelegraphâŠïļ</b>

Do as you wish with telegra.ph module!

</b>USAGE:</b>

ðĪ§ /telegraph - Send me Picture or Vide Under (5MB)

<b>NOTE:</b>

âĒ This Command Is Available in goups and pms
âĒ This Command Can be used by everyone"""
    JSON_TXT ="""<b>JSON:</b>

Bot returns json for all replied messages with /json

<b>Features:</b>

Message Editting JSON
Pm Support
Group Support

<b>Note:</b>

Everyone can use this command , if spaming happens bot will automatically ban you from the group."""
    PURGE_TXT = """<b>ðĢPurgeðĢ</b>
    
Delete A Lot Of Messages From Groups! 
    
 <b>ADMIN</b> 

â /purge :- Delete All Messages From The Replied To Message, To The Current Message"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Eva Maria Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. Eva Maria supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/+veUIdIW2CQ5mOGU5)</code>

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
âĒ /connect  - <code>connect a particular chat to your PM</code>
âĒ /disconnect  - <code>disconnect from a chat</code>
âĒ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
these are the extra features of Eva Maria

<b>Commands and Usage:</b>
âĒ /id - <code>get id of a specifed user.</code>
âĒ /info  - <code>get information about a user.</code>
âĒ /imdb  - <code>get the film information from IMDb source.</code>
âĒ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
âĒ /logs - <code>to get the rescent errors</code>
âĒ /stats - <code>to get status of files in db.</code>
âĒ /delete - <code>to delete a specific file from db.</code>
âĒ /users - <code>to get list of my users and ids.</code>
âĒ /chats - <code>to get list of the my chats and ids </code>
âĒ /leave  - <code>to leave from a chat.</code>
âĒ /disable  -  <code>do disable a chat.</code>
âĒ /ban_user  - <code>to ban a user.</code>
âĒ /unban_user  - <code>to unban a user.</code>
âĒ /channel - <code>to get list of total connected channels</code>
âĒ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """<b>áâš ððūðð°ðŧ ðĩðļðŧðīð: <code>{}</code></b>
<b>áâš ððūðð°ðŧ ðððīðð: <code>{}</code></b>
<b>áâš ððūðð°ðŧ ðēð·ð°ðð: <code>{}</code></b>
<b>áâš ðððīðģ ðððūðð°ðķðī: <code>{}</code> ðžðą</b>
<b>áâš ðĩððīðī ðððūðð°ðķðī: <code>{}</code> ðžðą</b>"""
    LOG_TEXT_G = """#ððð°ððŦðĻðŪðĐ
    
<b>áâš ððŦðĻðŪðĐ âŠž {}(<code>{}</code>)</b>
<b>áâš ððĻð­ððĨ ðððĶðððŦðŽ âŠž <code>{}</code></b>
<b>áâš ððððð ððē âŠž {}</b>
"""
    LOG_TEXT_P = """#ððð°ððŽððŦ
    
<b>áâš ðð - <code>{}</code></b>
<b>áâš ðððĶð - {}</b>
"""
    REPORT_TXT = """âĪ ðððĨðĐ: RáīáīáīĘáī â ïļ

ðððð ððððððð ððððð ðĒðð ðð ðððððð ð ððððððð ðð ð ðððð ðð ððð ðððððð ðð ððð ðððððððððð ððððð. ðģðð'ð ðððððð ðððð ððððððð.

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ/report ðð @admins - ðģð ððūðððð ðš ðððūð ðð ðððū ðšð―ðððð (ððūððð ðð ðš ððūðððšððū)."""

    CORONA_TXT = """âĪ ðððĨðĐ: ðĒðððð―

ðððð ðēðððððð ððððð ðĒðð ðð ðððð  ðððððĒ ððððððððððð ððððð ððððð 

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ /covid - ðððū ðððð ðžððððšðð― ðððð ðððð ðžðððððð ððšððū ðð ððūð ðžðððð―ðū ðððŋððððšðððð

âðĪððšððððū:
/covid ðĻðð―ððš"""

    URLSHORT_TXT = """âĪ ðððĨðĐ: ðīðð ðððððððūð

ðððð ððððððð ððððð ðĒðð ðð ððððð ð ððð 

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ /short: ðððū ðððð ðžððððšðð― ðððð ðððð ðððð ðð ððūð ððððððūð― ððððð

âðĪððšððððū:
/short https://t.me/+veUIdIW2CQ5mOGU5"""

    VIDEO_TXT ="""ð·ðīðŧðŋ ððūð ððū ðģðūðð―ðŧðūð°ðģ ððļðģðīðū ðĩððūðž ððūððððąðī.

âĒ ððīðĒðĻðĶ
ð ð°ðķ ððĒðŊ ðð°ðļðŊð­ð°ðĒðĨ ððŊðš ððŠðĨðĶð° ððģð°ðŪ ð ð°ðķðĩðķðĢðĶ

ððĪðŽ ððĪ ððĻð
âĒ ððšðąðĶ /video or /mp4 ððŊðĨ (ððŠðĨðĶð° Link)
âĒ ððđðĒðŪðąð­ðĶ:
/ðŪðą4 https://youtu.be/Your Link"""

    ZOMBIES_TXT = """ð·ðīðŧðŋ ððūð ððū ðšðļðēðš ðððīðð

<b>Kick incative members from group. Add me as admin with ban users permission in group.</b>

<b>Commands and Usage:</b>
âĒ /inkick - command with required arguments and i will kick members from group.
âĒ /instatus - to check current status of chat member from group.
âĒ /inkick within_month long_time_ago - to kick users who are offline for more than 6-7 days.
âĒ /inkick long_time_ago - to kick members who are offline for more than a month and Deleted Accounts.
âĒ /dkick - to kick deleted accounts."""

    IMAGE_TXT = """âĪ ðððĨðĐ: IáīáīÉĒáī

ðððð ððððððð ððððð ðĒðð ðð ðððð ððððð ððððĒ ððððððĒ 

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ ðĐððð ððūðð― ððū ðš ðððšððū ðð ðūð―ðð âĻ

ðŽðšð―ðū ðŧð <a href=https://t.me/+veUIdIW2CQ5mOGU5>ðð ððĐððð­ððŽ</a>"""

    STICKER_TXT = """ððūð ðēð°ð― ðððī ðð·ðļð ðžðūðģððŧðī ððū ðĩðļð―ðģ ð°ð―ð ðððļðēðšðīðð ðļðģ.
âĒ ððððð
To Get Sticker ID
 
  â­ ððĪðŽ ððĪ ððĻð
 
â Reply To Any Sticker [/stickerid]"""

    YTTHUMB_TXT = """ð·ðīðŧðŋð ððū ðģðūðð―ðŧðūð°ðģ ð°ð―ð ððūððððąðī ððļðģðīðū ðð·ððžðąð―ð°ðļðŧ
    
â­ððĪðŽ ððĪ ððĻð
ððšðąðĶ /ytthumb ððŊðĨ ððŠðĨðĶð° ððŠðŊðŽ

âĒ ððđðĒðŪðąð­ðĶ
/ytthumb https://youtu.be/yourlink"""

    ABOOK_TXT = """âĪ ðððĨðĐ: ð ðð―ðððŧððð

ððð ððð ððððððð ð ðŋðģðĩ ðððð ðð ð ððððð ðððð ð ððð ðððð ððððððð âŊ

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ /audiobook: ðąðūððð ðððð ðžððððšðð― ðð ðšðð ðŊðĢðĨ ðð ððūððūððšððū ðððū ðšðð―ðð"""

    GTRANS_TXT = """âĪ ðððĨðĐ: ðĶðððððū ðģððšððððšððūð

ðððð ððððððð ððððð ðĒðð ðð ððððððððð ð ðððĄð ðð ðšðð ððððððððð ðĒðð ð ððð. ðððð ððððððð ð ðððð ðð ðððð ðð ððð ððððð âŊ

âĪ ððĻðĶðĶðð§ððŽ ðð§ð ððŽðð ð:

âŠ/tr - ðģð ðððšððððšððūð ððūððð ðð ðš ðððūðžððŋðž ððšððððšððū

âĪ ð­ðððū:
ðķððððū ððððð /tr ððð ðððððð― ðððūðžððŋð ðððū ððšððððšððū ðžðð―ðū

âðĪððšððððū: /ðð ðð
âĒ ðūð = ðĪðððððð
âĒ ðð = ðŽðšððšððšððšð
âĒ ðð = ð§ððð―ð"""

    RESTRIC_TXT = """âĪ ðððĨðĐ: Máīáīáī ðŦ

ððððð ððð ððð ðððððððð ð ððððð ððððð ððð ððð ðð ðððððð ððððð ððððð ðððð ðððððððððððĒ.

âŠ/ban: ðģð ðŧðšð ðš ðððūð ðŋððð ðððū ððððð.
âŠ/unban: ðģð ðððŧðšð ðš ðððūð ðð ðððū ððððð.
âŠ/tban: ðģð ððūðððððšðððð ðŧðšð ðš ðððūð.
âŠ/mute: ðģð ððððū ðš ðððūð ðð ðððū ððððð.
âŠ/unmute: ðģð ððððððū ðš ðððūð ðð ðððū ððððð.
âŠ/tmute: ðģð ððūðððððšðððð ððððū ðš ðððūð.

âĪ ð­ðððū:
ðķððððū ððððð /tmute ðð /tban ððð ðððððð― ðððūðžððŋð ðððū ððððū ððððð.

âðĪððšððððū: /ððŧðšð 2ð― ðð /ðððððū 2ð―.
ðļðð ðžðšð ðððū ððšðððūð: ð/ð/ð―. 
 âĒ ð = ððððððūð
 âĒ ð = ððððð
 âĒ ð― = ð―ðšðð"""
    CREATOR_REQUIRED = """â<b>You have To Be The Group Creator To Do That.</b>"""
      
    INPUT_REQUIRED = "â **Arguments Required**"
      
    KICKED = """âïļ Successfully Kicked {} Members According To The Arguments Provided."""
      
    START_KICK = """ðŪ Removing Inactive Members This May Take A While..."""
      
    ADMIN_REQUIRED = """â<b>āīāīĻāĩāīĻāĩ Admin āīāīāĩāīāīĪāĩāīĪ āīļāĩāīĨāīēāīĪāĩāīĪāĩ āīāīūāĩŧ āīĻāīŋāīāĩāīāīŋāīēāĩāīē āīŠāĩāīāĩāīĩāīū Bii..Add Me Again with all admin rights.</b>"""
      
    DKICK = """âïļ Kicked {} Deleted Accounts Successfully."""
      
    FETCHING_INFO = """<b>āīāīŠāĩāīŠāĩ āīāīēāĩāīēāīūāī āīāīāīŋāīāĩāīāĩāīŪāīūāīąāĩāīąāīŋ āīĪāī°āīūāī...</b>"""
      
    STATUS = """{}\n<b>Chat Member Status</b>**\n\n```<i>Recently``` - {}\n```Within Week``` - {}\n```Within Month``` - {}\n```Long Time Ago``` - {}\nDeleted Account - {}\nBot - {}\nUnCached - {}</i>
"""
