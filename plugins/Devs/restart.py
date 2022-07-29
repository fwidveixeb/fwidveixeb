import heroku3
import asycnio
from Vars import Var
from info import ADMINS
from pyrogram import Client, Filters

#Getting Heroku API KEY and APP NAME from Vars
HEROKU_API_KEY = Var.HEROKU_API_KEY
HEROKU_APP_NAME = Var.HEROKU_APP_NAME

heroku = heroku3.from_key(HEROKU_API_KEY)
app = heroku.app(HEROKU_APP_NAME)

@Client.on_message(filters.command("restart") & filters.user(ADMINS))
async def restart(bot, message):
  
  k = await message.reply("`Restarting Bot... This may take time depending on the server.`"
  app.restart()
  await k.edit("Restarted Successfully, if I'm not working Check logs.") 
