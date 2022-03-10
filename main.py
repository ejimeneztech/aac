from ui import UserInterface
from api import data
from speaker import Speaker





post_text = data[0]["text"]
post_url = data[0]["url"]
post_image = 'https://audiopost-test.s3.us-west-2.amazonaws.com/wave.jpeg'




new_speaker = Speaker(post_text, post_url, post_image)


UI = UserInterface(new_speaker)