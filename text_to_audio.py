from gtts import gTTS

class TextToSpeech:
    def __init__(self, lang='en', tld='co.in'):
        """
        Initialize TextToSpeech with language and domain.
        :param lang: Language for speech synthesis (default: 'en')
        :param tld: Top-level domain for regional accent (default: 'co.in' for Indian accent)
        """
        self.lang = lang
        self.tld = tld

    def convert_text_to_audio(self, text, output_file="audio.mp3"):
        """
        Convert text to speech and save the audio file.
        :param text: The text to be converted to speech
        :param output_file: Name of the output audio file
        """
        try:
            tts = gTTS(text=text, lang=self.lang, tld=self.tld)
            tts.save(output_file)
            print(f"Audio saved as {output_file}")
            return True
        except Exception as e:
            print(f"Error in audio converter: {e}")
            return False


