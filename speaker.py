import vlc

class Speaker:
    def __init__(self, speaker_text, speaker_url):
        self.text = speaker_text
        self.url = speaker_url
    

    def play_audio(self):
        p = vlc.MediaPlayer(self.url)
        p.play()