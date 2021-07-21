from pyrogram import Client
from pyrogram import Filters
import shelve

db = shelve.open('data.db', writeback=True)

API_ID = 7392863
API_HASH = 'de5b8045f9c7f99bc526c167d77d2b28'

PRIVATE_PUBLIC = 'jdfjfsdf'
PUBLIC_PUBLIC = 'fresh_meme'
SOURCE_PUBLICS = ['dvachannel', 'community_memy','nauka_anekdoty1']







PHONE_NUMBER = '+79393438122'



app = Client("cyberya", api_id=API_ID,
             api_hash=API_HASH,
             phone_number=PHONE_NUMBER)


@app.on_message(Filters.chat(SOURCE_PUBLICS))
def new_channel_post(client, message):
    post_id = add_post_to_db(message)
    