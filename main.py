from ui import UserInterface
from api import data
from speaker import Speaker

post_list = []
for post in data:
    post_text = post["text"]
    post_url = post["url"]
    new_speaker = Speaker(post_text, post_url)


UI = UserInterface()