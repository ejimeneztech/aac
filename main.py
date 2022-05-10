from ui import UserInterface
from api import data
from speaker import Speaker




post_text = data[0]["text"]
post_url = data[0]["url"]
post_image = data[0]["img_url"]




new_speaker = Speaker(post_text, post_url, post_image)


UI = UserInterface(new_speaker)