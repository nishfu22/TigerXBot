
"""

💐 Commands Available -

• `{i}wiki <search query>``
    Wikipedia search from telegram.

"""

import wikipedia

from . import *


@ilhammansiz_cmd(pattern="wiki ?(.*)")
async def wiki(e):
    srch = e.pattern_match.group(1)
    if not srch:
        return await eor(e, "`Give some text to search on wikipedia !`")
    msg = await eor(e, f"`Searching {srch} on wikipedia..`")
    try:
        mk = wikipedia.summary(srch)
        te = f"**Search Query :** {srch}\n\n**Results :** {mk}"
        await msg.edit(te)
    except Exception as e:
        await msg.edit(f"**ERROR** : {str(e)}")
