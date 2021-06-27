
"""
💐 Commands Available -

•`{i}htg <text>`
   How To Google.
   Some peoples don't know how to google so help them 🙃🙂.

•`{i}doodle`
   Get Today's Google Doodle.
"""


import requests
from bs4 import BeautifulSoup as bs

from . import *


@ilhammansiz_cmd(pattern="htg ?(.*)")
async def _(e):
    text = e.pattern_match.group(1)
    if not text:
        return await eod(e, "`Give some text`")
    url = "https://da.gd/s?url=https://lmgtfy.com/?q={}%26iie=1".format(
        text.replace(" ", "+")
    )
    response = requests.get(url).text
    if response:
        await eor(e, "[{}]({})\n`Thank me Later 🙃` ".format(text, response.rstrip()))
    else:
        await eod(e, "`something is wrong. please try again later.`")


@ilhammansiz_cmd(pattern="doodle$")
async def gdoodle(event):
    cont = requests.get("https://google.com").content
    try:
        bst = bs(cont, "html.parser", from_encoding="utf-8")
        m = bst.find_all("meta", {"property":"twitter:image"})
        await event.reply(caption="Here is Today's Google Doodle", file=m[0]["content"])
        if event.out:
            await event.delete()
    except:
        await eor(event, "`FAILED to Get Google Doodle.`")
