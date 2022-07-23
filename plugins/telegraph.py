import os
import requests
from pyrogram import Client, filters
from telegraph import upload_file

@Client.on_message(filters.command("telegraph"))
async def telegraph(bot, message):
    
    replied = message.reply_to_message
    
    if replied.photo:
        p = await message.reply("Downloading...")
        user_id = str(message.chat.id)
        img_path = (f"./DOWNLOADS/{user_id}.jpg")
        img_download = await bot.download_media(message=replied, file_name=img_path)
        await p.edit("Uploading...")
        try:         
            tgraph_img = upload_file(img_download)
            await p.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_img[0]}", disable_web_page_preview=True)     
            os.remove(img_download) 
        except Exception as e:
            await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat")
            
    elif replied.video:
        if replied.video.file_size < 5242880:
            a = await message.reply_text("Downloading...")
            user_id = str(message.chat.id)
            vid_path = (f"./DOWNLOADS/{user_id}.mp4")
            vid_download = await bot.download_media(message=replied, file_name=vid_path)
            await a.edit("Uploading...")
            try:
                tgraph_vid = upload_file(vid_download)
                await a.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_vid[0]}", disable_web_page_preview=True)     
                os.remove(vid_download) 
            except Exception as e:
                await a.delete()
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat.")
        else:
            await message.reply("Size must be less than 5 Mb, it's Telegraph's limit not ours.")
            
    elif replied.animation:
        if replied.animation.file_size < 5242880:
            g = await message.reply("Downloading...")
            user_id = str(message.chat.id)
            gif_path = (f"./DOWNLOADS/{user_id}.mp4")
            gif_download = await bot.download_media(message=replied, file_name=gif_path)
            await g.edit("Uploading...")
            try:
                tgraph_gif = upload_file(gif_download)
                await g.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_gif[0]}", disable_web_page_preview=True)     
                os.remove(gif_download) 
            except Exception as e:
                await g.delete()
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat.")
        else:
            await message.reply("Size must be less than 5 Mb, it's Telegraph's limit not ours.")
    elif replied.sticker:
        if replied.sticker.is_video==True:
            s = await message.reply("Downloading...")
            user_id = str(message.chat.id)
            sti_path = (f"./DOWNLOADS/{user_id}.mp4")
            sti_download = await bot.download_media(message=replied, file_name=sti_path)
            await s.edit("Uploading...")
            try:
                tgraph_sti = upload_file(sti_download)
                await s.edit(f"Here is your link:\n\nhttps://telegra.ph{tgraph_sti[0]}", disable_web_page_preview=True)     
                os.remove(sti_download) 
            except Exception as e:
                await s.delete()
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat.")
        elif replied.sticker.is_animated==True:
            n = await message.reply("Downloading...")
            user_id = str(message.chat.id)
            _sti_path = (f"./DOWNLOADS/{user_id}.mp4")
            _sti_download = await bot.download_media(message=replied, file_name=_sti_path)
            await n.edit("Uploading...")
            try:
                _tgraph_sti = upload_file(_sti_download)
                await n.edit(f"Here is your link:\n\nhttps://telegra.ph{_tgraph_sti[0]}", disable_web_page_preview=True)     
                os.remove(_sti_download) 
            except Exception as e:
                await n.delete()
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat.")
        else:
            m = await message.reply("Downloading...")
            user_id = str(message.chat.id)
            _sti_path_ = (f"./DOWNLOADS/{user_id}.jpg")
            _sti_download_ = await bot.download_media(message=replied, file_name=_sti_path_)
            await m.edit("Uploading...")
            try:
                _tgraph_sti_ = upload_file(_sti_download_)
                await m.edit(f"Here is your link:\n\nhttps://telegra.ph{_tgraph_sti_[0]}", disable_web_page_preview=True)     
                os.remove(_sti_download_) 
            except Exception as e:
                await m.delete()
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaChat.")
    elif replied:
        b = await message.reply("Downloading...")
            user_id = str(message.chat.id)
            doc_path = (f"./DOWNLOADS/{user_id}.jpg")
            doc_download = await bot.download_media(message=replied, file_name=doc_path)
            await b.edit("Uploading...")
            ab = open(doc_download)
            cd = ab.read()
            ab.close()
            try:
                API = "https://api.telegra.ph/createPage"
                access_token = "137c591d35dcb4075767daeb4a2c48520657074b769a5aa1bdbe6fb848dd"
                title = "Hagadmansa"
                author_name = "Hagadmansa"
                author_url = "https://hagadmansa.com"
                makeit = requests.get(f"https://api.telegra.ph/createPage?access_token={access_token}&title={title}&author_name={author_name}&author_url={author_url}&content=%5B%7B%22tag%22:%22p%22,%22children%22:%5B%22{replied.text}%22%5D%7D%5D&return_content=true").json()
                war = makeit["result"]["url"]
                await b.edit(f"Here is your link:\n\nhttps://telegra.ph{war}", disable_web_page_preview=True)
                os.remove(doc_download)
            except Exception as e:
                await b.delete()
                await message.reply(f"#Error {e}\n\n Forward this to @HagadmansaBot.")
            
            
            
