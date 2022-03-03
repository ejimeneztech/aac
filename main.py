from ui import UserInterface
from api import data
from speaker import Speaker

post_text = data[0]["text"]
post_url = data[0]["url"]
new_speaker = Speaker(post_text, post_url)


UI = UserInterface(new_speaker)