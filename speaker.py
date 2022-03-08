import vlc

class Speaker:
    def __init__(self, speaker_text, speaker_url):
        self.text = speaker_text
        self.url = speaker_url
    

    def play_audio(self):
        # playsound('')
        p = vlc.MediaPlayer("https://audiopost-test.s3.us-west-2.amazonaws.com/fec2458a-deff-4ef4-bc1a-8901f238d847.mp3")
        p.play()