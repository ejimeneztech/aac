from playsound import playsound



class Speaker:
    def __init__(self, speaker_text, speaker_url):
        self.text = speaker_text
        self.url = speaker_url
    

    def play_audio(self):
        playsound('https://s3-us-west-2.amazonaws.com/audiopost-test/fec2458a-deff-4ef4-bc1a-8901f238d847.mp3')
        