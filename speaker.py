import vlc

class Speaker:
    def __init__(self, speaker_text, speaker_url, speaker_image):
        self.text = speaker_text
        self.url = speaker_url
        self.image = speaker_image

    def play_audio(self):
        p = vlc.MediaPlayer(self.url)
        p.play()